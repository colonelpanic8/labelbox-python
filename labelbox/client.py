import json
import logging
import os
import urllib.request

from labelbox import query
from labelbox.exceptions import (NetworkError, AuthenticationError,
                                 ResourceNotFoundError)
from labelbox.db_objects import Project, Dataset


logger = logging.getLogger(__name__)


class Client:
    """ A Labelbox client. Containes info necessary for connecting to
    the server (URL, authentication key). Provides functions for querying
    and creating top-level data objects (Projects, Datasets).
    """

    def __init__(self, api_key=None,
                 endpoint='https://api.labelbox.com/graphql'):
        """ Create and initialize a Labelbox Client.

        Args:
            api_key (str): API key. If None, the key is obtained from
                the "LABELBOX_API_KEY" environment variable.
            endpoint (str): URL of the Labelbox server to connect to.
        """
        if api_key is None:
            api_key = os.environ["LABELBOX_API_KEY"]

        self.endpoint = endpoint
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % api_key}

    def execute(self, query, variables=None):
        """ Execute a GraphQL query on the server.

        Args:
            query: str, the query to execute.
            variables: dict, variables referenced within the query.
        Return:
            dict, parsed JSON response.
        Raises:
            labelbox.exception.NetworkError: If an urllib.error.HTTPError
                occurred.
            labelbox.exception.AuthenticationError: If authentication
                failed.
        """
        logger.debug("Query: %s", query)
        data = json.dumps({'query': query, 'variables': variables}).encode('utf-8')
        req = urllib.request.Request(self.endpoint, data, self.headers)

        try:
            response = urllib.request.urlopen(req)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            # Convert HTTPError into a Labelbox error
            raise NetworkError(e)

    def get_single(self, db_object_type, uid):
        """ Fetches a single object of the given type, for the given ID.

        Args:
            db_object_type (type): DbObject subclass.
            uid (str): Unique ID of the row.
        Return:
            Object of `db_object_type`.
        Raises:
            labelbox.exception.ResourceNotFoundError: If there is no object
                of the given type for the given ID.
            labelbox.exception.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        query_str, id_param_name = query.get_single(db_object_type)
        params = {id_param_name: uid}
        res = self.execute(query_str, params)["data"][
            db_object_type.type_name().lower()]
        if res is None:
            raise ResourceNotFoundError(db_object_type, params)
        else:
            return db_object_type(self, res)


    def get_project(self, project_id):
        """ Convenience for `client.get_single(Project, project_id)`. """
        return self.get_single(Project, project_id)

    def get_dataset(self, dataset_id):
        """ Convenience for `client.get_single(Dataset, dataset_id)`. """
        return self.get_single(Dataset, dataset_id)

    def get_projects(self):
        """ Fetches all the projects the user has access to.

        Return:
            An iterable of Projects (typically a PaginatedCollection).
        Raises:
            labelbox.exception.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        return query.PaginatedCollection(
            self, query.get_all(Project), {}, ["projects"], Project)

    def get_datasets(self):
        """ Fetches all the datasets the user has access to.

        Return:
            An iterable of Datasets (typically a PaginatedCollection).
        Raises:
            labelbox.exception.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        return query.PaginatedCollection(
            self, query.get_all(Dataset), {}, ["datasets"], Dataset)
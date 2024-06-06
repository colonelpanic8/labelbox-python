const core = require('@actions/core');

try {
  const files = JSON.parse(core.getInput('files-changed'));
  const startingMatrix = [
    {
      "python-version": "3.8",
      "api-key": "STAGING_LABELBOX_API_KEY_2",
      "da-test-key": "DA_GCP_LABELBOX_API_KEY"
    },
    {
      "python-version": "3.9",
      "api-key": "STAGING_LABELBOX_API_KEY_3",
      "da-test-key": "DA_GCP_LABELBOX_API_KEY"
    },
    {
      "python-version": "3.10",
      "api-key": "STAGING_LABELBOX_API_KEY_4",
      "da-test-key": "DA_GCP_LABELBOX_API_KEY"
    },
    {
      "python-version": "3.11",
      "api-key": "STAGING_LABELBOX_API_KEY",
      "da-test-key": "DA_GCP_LABELBOX_API_KEY"
    },
    {
      "python-version": "3.12",
      "api-key": "STAGING_LABELBOX_API_KEY_5",
      "da-test-key": "DA_GCP_LABELBOX_API_KEY"
    }
  ];
  const finalMatrix = [];
  files.forEach(file => {
    startingMatrix.forEach(matrixItem => {
      finalMatrix.push({
        ...matrixItem,
        package: files.split('/')[1]
      });
    });
  });
  core.setOutput("matrix", JSON.stringify(finalMatrix));
} catch {
    core.setFailed("Could not create matrix");
}
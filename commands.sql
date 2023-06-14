CREATE OR REPLACE TABLE RECRUTE (
  index int,
  poste VARCHAR,
  Location VARCHAR,
  date_publication VARCHAR,
  delai VARCHAR,
  genre VARCHAR,
  lien_publication VARCHAR,
  Entreprise VARCHAR
);

CREATE OR REPLACE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN='arn:aws:iam::360002118275:role/mys3role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://hajarbucketaws/data/')

  CREATE OR REPLACE STAGE my_s3_stage URL = 's3://hajarbucketaws/data/donnees.csv' STORAGE_INTEGRATION = s3_int;


  CREATE OR REPLACE FILE FORMAT my_csv_format
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  RECORD_DELIMITER = '\n'
  SKIP_HEADER = 0
  ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE;


  COPY INTO RECRUTE
FROM @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
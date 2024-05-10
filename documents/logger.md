# Logger Documentation

## Overview
This documentation describes the logging setup used in the SuRFM package. The logger module includes a custom formatter that enhances log readability by using colors to differentiate the severity levels of log messages.

## Logger Configuration
The logging system uses the `logging` module from Python's standard library and is extended by a custom formatter class, which adds colors to the logs based on their severity levels.

### CustomFormatter Class
- **Purpose**: Enhances log readability by applying color coding to different log levels.
- **Colors**:
    - Grey: DEBUG
    - Violet: INFO
    - Yellow: WARNING
    - Red: ERROR
    - Bold Red: CRITICAL

### Log Format
Each log entry includes the timestamp, logger name, function name, log level, message, and the line number. The date and time format is set to `YYYY-MM-DD HH:MM:SS`.

## File Handlers
- **StreamHandler**: Outputs logs to the console with the same formatting as file logs.
- **RotatingFileHandler**:
    - **File Name**: `{logger_name}.log`, where `logger_name` is the filename of the script minus the file extension.
    - **Rotation Criteria**: The log file is rotated when it reaches 10 KB. Up to three backup files are kept.

## Usage Example
Below is an example of how to configure the logger in a Python script:

```python
import logging
from logger import CustomFormatter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console handler with custom formatter
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

# File handler with custom formatter and rotation
fh = RotatingFileHandler('application.log', maxBytes=10240, backupCount=3)
fh.setLevel(logging.DEBUG)
fh.setFormatter(CustomFormatter())
logger.addHandler(fh)

# Test logging
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

Additional Notes
Ensure that the RotatingFileHandler directory path is accessible and writable.
Adjust log levels and handlers as necessary based on the deployment environment or debugging needs.
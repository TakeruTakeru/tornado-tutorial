from tornado import httpclient
from logging import getLogger, INFO

logger = getLogger(__package__)


if __name__ == '__main__':
    http_client = httpclient.HTTPClient()
    try:
        response = http_client.fetch("https://anonymous-boilerplate.firebaseapp.com")
        logger.info(response.body)
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()
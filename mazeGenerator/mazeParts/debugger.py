import logging


class Debugger(object):
    formatter = logging.Formatter("%(message)s")

    # LOGGER = logging.getLogger(__name__)
    # LOGGER.setLevel(logging.INFO)
    # file_handler = logging.FileHandler(log_file)
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.INFO)

    STREAMER = logging.getLogger(__name__)
    STREAMER.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)

    # LOGGER.addHandler(file_handler)
    STREAMER.addHandler(stream_handler)

import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        data_read = super().readline()
        if data_read:
            self._read_bytes += len(data_read)
            self._read_ops += 1
            return data_read
        else:
            raise StopIteration

    def read(self, size=-1):
        data_read = super().read(size)
        self._read_bytes += len(data_read)
        self._read_ops += 1
        return data_read

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        data_write = super().write(b)
        self._write_bytes += data_write
        self._write_ops += 1
        return data_write

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        recv_data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(recv_data)
        self._recv_ops += 1
        return recv_data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        data_send = self._socket.send(data, flags)
        self._send_bytes += data_send
        self._send_ops += 1
        return data_send

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops

# P2_B.py
# Part B: Implement six core RLE helper functions (no main method required).
# Functions:
#   - to_hex_string
#   - count_runs
#   - encode_rle
#   - get_decoded_length
#   - decode_rle
#   - string_to_data

def _hex_digit(n: int) -> str:
    """Return a single lowercase hex digit for 0 <= n <= 15."""
    if 0 <= n <= 9:
        return chr(ord('0') + n)
    if 10 <= n <= 15:
        return chr(ord('a') + (n - 10))
    raise ValueError("hex digit out of range: {}".format(n))

def _from_hex_char(c: str) -> int:
    """Convert one hex character to its integer 0..15 value (case-insensitive)."""
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    c_low = c.lower()
    if 'a' <= c_low <= 'f':
        return 10 + (ord(c_low) - ord('a'))
    raise ValueError("invalid hex character: {!r}".format(c))

def to_hex_string(data):
    """
    Translates data (RLE or raw) to a hexadecimal string (no delimiters).
    Example: to_hex_string([3,15,6,4]) -> '3f64'
    """
    return ''.join(_hex_digit(x) for x in data)

def count_runs(flat_data):
    """
    Returns number of runs of data in an image data set; runs are capped at 15.
    Example: count_runs([15,15,15,4,4,4,4,4,4]) -> 2
    """
    if not flat_data:
        return 0

    runs = 0
    current = flat_data[0]
    length = 0

    for v in flat_data:
        if v == current and length < 15:
            length += 1
        else:
            # finalize the previous run
            runs += 1
            # start new run
            current = v
            length = 1
        # if we hit 15, we must close the run even if the next value is the same
        if length == 15:
            runs += 1
            length = 0  # will be set to 1 when a different value arrives, or next same splits

            # Special handling: if next value is same, we'll start a new run of same color.
            # We "prime" current so loop logic continues correctly.
            # (No-op here because current stays as v; length reset makes a new run next iter.)

    # If we ended mid-run (length in 1..14), count it
    if 1 <= length <= 14:
        runs += 1
    return runs

def encode_rle(flat_data):
    """
    Returns RLE encoding [count, value, count, value, ...] of flat_data.
    Runs cannot be longer than 15; longer runs are split into 15-sized chunks.
    Example: encode_rle([15,15,15,4,4,4,4,4,4]) -> [3,15,6,4]
    """
    if not flat_data:
        return []

    encoded = []
    current = flat_data[0]
    length = 0

    for v in flat_data:
        if v == current and length < 15:
            length += 1
        else:
            # flush previous run
            if length > 0:
                encoded.extend([length, current])
            # start new run
            current = v
            length = 1

        # split runs of length 15 immediately
        if length == 15:
            encoded.extend([15, current])
            length = 0  # reset to accumulate any subsequent same values

    # flush tail
    if length > 0:
        encoded.extend([length, current])

    return encoded

def get_decoded_length(rle_data):
    """
    Returns the decompressed length (number of flat pixels) of RLE data.
    Example: get_decoded_length([3,15,6,4]) -> 9
    """
    # rle_data format: [count0, value0, count1, value1, ...]
    # Sum just the counts (even indices)
    total = 0
    for i in range(0, len(rle_data), 2):
        total += rle_data[i]
    return total

def decode_rle(rle_data):
    """
    Returns the decoded flat list from RLE encoded data.
    Example: decode_rle([3,15,6,4]) -> [15,15,15,4,4,4,4,4,4]
    """
    decoded = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        decoded.extend([value] * count)
    return decoded

def string_to_data(data_string):
    """
    Translates a hexadecimal string into a list of ints (nibbles).
    Example: string_to_data('3f64') -> [3,15,6,4]
    """
    return [_from_hex_char(c) for c in data_string]

"""ChecksumCalculator demonstrating Connascence of Algorithm."""


# Connascence of Algorithm: the same checksum computation (sum of char
# codes mod 10) is duplicated in both methods instead of extracted once
# -- if the algorithm ever changes, both call sites must be updated in
# lockstep or they silently disagree.
class ChecksumCalculator:
    def add_checksum(self, input_data: str) -> str:
        checksum_sum = sum(ord(character) for character in input_data)
        checksum = checksum_sum % 10
        return f"{input_data}{checksum}"

    def check(self, input_data_with_checksum: str) -> bool:
        input_data = input_data_with_checksum[:-1]
        expected = int(input_data_with_checksum[-1])
        checksum_sum = sum(ord(character) for character in input_data)
        return checksum_sum % 10 == expected

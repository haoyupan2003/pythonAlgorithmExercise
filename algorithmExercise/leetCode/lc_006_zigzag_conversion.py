class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row (or string too short), zigzag does nothing
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [""] * numRows

        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Reverse direction if we hit top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        # Join all rows
        return "".join(rows)

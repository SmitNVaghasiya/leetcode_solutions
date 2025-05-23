class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            for j in range((n + 1) // 2):
                row[j], row[n - 1 - j] = row[n - 1 - j] ^ 1, row[j] ^ 1
        return image

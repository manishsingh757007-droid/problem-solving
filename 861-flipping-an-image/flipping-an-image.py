class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        for row in image:
           
            row.reverse()
           
            for i in range(n):
                row[i] ^= 1  
        return image

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    store = image[sr][sc]
    self.update_matrix(image, sr, sc, color, store)
    return image
  
  def update_matrix(self, image: List[List[int]], sr: int, sc: int, color: int, store: int):
    if (sr>= 0 and sr < len(image)) and (sc >= 0 and sc < len(image[0])) and (image[sr][sc] != store):
      return
    elif (sr>= 0 and sr < len(image)) and (sc >= 0 and sc < len(image[0])) and (image[sr][sc] != color):
      image[sr][sc] = color
      self.update_matrix(image, sr, sc-1, color, store)
      self.update_matrix(image, sr, sc+1, color, store)
      self.update_matrix(image, sr-1, sc, color, store)
      self.update_matrix(image, sr+1, sc, color, store)

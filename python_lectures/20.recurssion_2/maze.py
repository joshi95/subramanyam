# """
# Given a maze a rat is at starting position (0, 0)
# we have to find the no of ways in which it can reach 
# Destination
# """

# def NoOfWays(x, y, n, m, grid):
# 	if x >= n:
# 		return 0

# 	if y >= m:
# 		return 0

# 	if grid[x][y] == 1: # if there is a wall
# 		return 0

# 	if x == n - 1 and y == m - 1:
# 		return 1
		
# 	ans = NoOfWays(x, y + 1, n, m, grid) + NoOfWays(x + 1, y, n, m, grid)
# 	return ans

# if __name__ == '__main__':
# 	grid = [[0, 0, 1, 1], [1, 0, 0, 0], [1, 1, 0, 0]]
# 	n = len(grid)
# 	m = len(grid[0])
# 	print(NoOfWays(0, 0, n, m, grid))


def Tiling(N):
	print(N)
	Tiling(N)
	# if N < 0:
	# 	return 0

	# if N == 0:
	# 	return 1
	
	# ans = Tiling(N - 1) + Tiling(N - 2)
	# return ans

if __name__ == "__main__":
	print(Tiling(5))



review = []

with open("reviews.txt", "r") as f :
	for line in f :
		review.append(line)
print(len(review))

x = input("Please input how many reviews you want to print :")
x = int(x)
for ln in range(x) :
	print(ln + 1, " ", review[ln])

review_length = []
for l in range(len(review)) :
	y = len(review[l])
	review_length.append(y)
z = sum(review_length)/len(review)
print(z)

sum_length = 0
for d in review :
	sum_length += len(d)
average = sum_length/len(review)
print(average)

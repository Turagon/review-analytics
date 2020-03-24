review = []

with open("reviews.txt", "r") as f :
	for line in f :
		review.append(line)
print(len(review))

x = input("Please input how many reviews you want to print :")
x = int(x)
for ln in range(x) :
	print(ln + 1, " ", review[ln])

limit = input("Please input the limit length of each review you want to sort :")
limit = int(limit)

review_length = [len(d) for d in review]
review_short = [d for d in review if len(d) < limit]
review_long = [d for d in review if len(d) >= limit]
review_good = [d for d in review if "good" in d]

print(len(review_short))
print(len(review_long))
print(len(review_good))

z = sum(review_length)/len(review)
print(z)

sum_length = 0
for d in review :
	sum_length += len(d)
average = sum_length/len(review)
print(average)

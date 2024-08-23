work = {

	"Monday": 3,
	"Tuesday": 4, 
	"Wednesday": 2,
	"Thursday": 1, 
	"Friday": 1, 
	
}

work["Saturday"] = 1
work.pop("Wednesday")
print(len(work))

if "friday" in work:
	print("Friday is in work")

print(work)
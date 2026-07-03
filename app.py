from model import predict_approval

print("=== Credit Card Approval Prediction ===")

income = int(input("Enter your income: "))
age = int(input("Enter your age: "))

result = predict_approval(income, age)

if result[0] == 1:
    print("Result: Credit Card Approved ✅")
else:
    print("Result: Credit Card Rejected ❌")

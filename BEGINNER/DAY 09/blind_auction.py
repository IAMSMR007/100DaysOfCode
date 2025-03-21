from art import logo
print(logo)
print("Welcome to blind auction")
bid_detail={}
major_list=[]
winner=""v
while True:
    bidder_name=input("Enter Your Name : ")
    bid=int(input("Enter Your Bid :$"))
    bid_detail[bidder_name]=bid
    major_list.append(bid)
    ask=input("Is there are others who wants to bid. 'yes' or 'no' : ")
    if ask=="yes":
        print("\n"*20)
    else:
        maximum=max(major_list)
        for name in bid_detail:
            if bid_detail[name]==maximum:
                winner=name
        print(f"\n The Winner is {winner} with the bid of {maximum}")
        break

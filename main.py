# Final Project
# Shaan Kohli, CS 111, Reckinger
#This is a fun stock market game where the user 
#clicks on turtles as their options to see how 
#a random event affects their chosen
#company's stock price!

import turtle
import random

#defines all turtles used in program
s = turtle.Screen()
start_text_turtle = turtle.Turtle()
rules_text = turtle.Turtle()
round_1_text = turtle.Turtle()
name_turtle = turtle.Turtle()
text = turtle.Turtle()
stock_chosen = turtle.Turtle()
buy = turtle.Turtle()
sell = turtle.Turtle()
nothing = turtle.Turtle()
cat = turtle.Turtle()
current_cash_text = turtle.Turtle()
shares_owned_text = turtle.Turtle()
account_value_text = turtle.Turtle()
profit_loss = turtle.Turtle()
fireworks = turtle.Turtle()
celebrate_front = turtle.Turtle()
celebrate_back = turtle.Turtle()
celebration_text = turtle.Turtle()
sad = turtle.Turtle()
tears = turtle.Turtle()
sad_screen_text = turtle.Turtle()
results = turtle.Turtle()

#dictionary for stock prices for all companies
stock_price_dict = {
  "Apple": 160.65, 
  "Amazon": 99.34,
  "Meta": 214.34,
  "Google": 105.67,
  "Microsoft": 282.33,
  "Netflix": 331.03,
  "Walmart": 150.57,
  "Disney": 97.94,
  "Starbucks": 105.60,
  "Tesla": 187.22
}

#starting values for user
shares_owned = 10
current_cash = 100000

#initializes profit / loss
starting_profit_loss = 0

#makes event displayed a random color
colors = ["blue", "red", "yellow", "orange", "purple", "green"]
random_color = random.choice(colors)

def start_screen():

  #text in the start menu
  s.bgpic("optiver.gif")
  start_text_turtle.penup()
  start_text_turtle.goto(0, 120)
  start_text_turtle.pencolor("green")
  start_text_turtle.write("Stock Market Game Presented By", align = "center", font = ("Arial", 27, "bold"))
  start_text_turtle.goto(0, -175)
  start_text_turtle.write("Check the terminal to see the rules", align="center", font = ("Arial", 24, "bold"))

def turtle_on_screen_during_game():
  #adds turtle for buy option
  s.addshape("buy.gif")
  buy.shape("buy.gif")
  buy.penup()
  buy.goto(250, 90)

  #adds turtle for sell option
  s.addshape("sell.gif")
  sell.shape("sell.gif")
  sell.penup()
  sell.goto(250, -70)

  #adds turtle to do nothing
  s.addshape("nothing.gif")
  nothing.shape("nothing.gif")
  nothing.penup()
  nothing.goto(250, -180)

  #adds cat character 
  s.addshape("cat.gif")
  cat.shape("cat.gif")
  cat.penup()
  cat.goto(-280, 10)

#clears rules screen on click
def clear_rules_screen(x, y):
  s.bgpic(None)
  s.clearscreen()

#function to clear any screen when needed
def clear_screen():
  s.bgpic(None)
  s.clearscreen()

#pulls up rules screen
def rules_screen():
  print()
  print("The rules of the game are as follows:")
  print()
  print("An event will be displayed at the top of your screen.")
  print("Buy, sell, or do neither by clicking on the image \ncorresponding to your option.")
  print("Think carefully about how the event might impact \nthe price of your chosen stock.")
  print("You cannot buy or sell more than 5 shares at a time.")
  print("After you choose an option, click the results button \nto see your profits / loss.")
  print("Clicking on more than 1 option will not work so \nchoose carefully.")
  print("Remember the most important phrase: Buy low, Sell high.")
  print("Please enter your username and company below.")
  print()

#puts the username inside the cat
def name_in_cat():
  name_turtle.penup()
  name_turtle.goto(-275, -15)
  name_turtle.write(name, align="center", font = ("Arial", 14, "bold"))

#brings in events and stock price impact data
def load_events():
  file = open("events_stock.py")
  events = {}
  
  for line in file:
    event, impact = line.strip().split(",")
    events[event] = float(impact)

  return events

#function to choose a random event
def random_event():
  
  event_random = list(all_events.keys())
  return random.choice(event_random)

#creates turtle for event showing up on screen
def event_on_screen():
  text.penup()
  text.goto(0, 175)
  text.pencolor(random_color)
  text.write(event_at_random, align = "center", font = ("Arial", 20, "bold"))

#text for which stock user selected
def stock_chosen_text():
  stock_chosen.penup()
  stock_chosen.goto(-280, 120)
  stock_chosen.pencolor(random_color)
  stock_chosen.write("You chose: " + stock_input, align = "center", font = ("Arial", 14, "bold"))
  stock_chosen.goto(-280, 90)
  stock_chosen.write("Original Price: $" + str(stock_price_dict[stock_input]), align = "center", font = ("Arial", 14, "bold"))

#current cash text on screen
def update_current_cash():
  global current_cash

  if current_cash < 0:
    current_cash = 0

  current_cash_text.penup()
  current_cash_text.pencolor(random_color)
  current_cash_text.goto(-280, -140)
  current_cash_text.clear()
  current_cash_text.write("Current Cash: ${:.2f}".format(current_cash), align = "center", font = ("Arial", 14, "bold"))

# turtle for shares owned text on screen 
def update_shares_owned():
  global shares_owned
 
  if shares_owned > 20:
    shares_owned = 20
  elif shares_owned < 0:
    shares_owned = 0

  shares_owned_text.penup()
  shares_owned_text.pencolor(random_color)
  shares_owned_text.goto(-280, -100)
  shares_owned_text.clear()
  shares_owned_text.write("Shares Owned: " + str(shares_owned), align = "center", font = ("Arial", 14, "bold"))

#starts off with $0 profit
def initial_profit_loss():
  profit_loss.penup()
  profit_loss.pencolor(random_color)
  profit_loss.goto(-280, -220)
  profit_loss.clear()
  profit_loss.write("Profit / Loss: $" + str(starting_profit_loss), align = "center", font = ("Arial", 14, "bold"))
  
#user chooses how many shares they want to buy
def click_to_buy(x, y):
  global shares_owned, current_cash, new_price
  
  shares_to_buy = input("How many shares would you like to buy? ")
  while shares_to_buy.isdigit() == False:
    shares_to_buy = input("Please enter a valid amount of shares: ")
  
  while int(shares_to_buy) > 5:
    shares_to_buy = input("You can only purchase up to 5 shares at a time. Please enter a valid amount of shares: ")
  
  while int(int(shares_to_buy) + shares_owned) > 20:
    shares_to_buy = input("You cannot have more than 20 shares at a time. Please enter a valid number: ")
  shares_to_buy = int(shares_to_buy)

  shares_owned += shares_to_buy

  current_cash -= shares_to_buy * new_price

  #updates shares and cash on screen
  update_shares_owned()
  update_current_cash()
  update_account_value()
  update_profit_loss()

  print()
  print("Click on the results!")


#user chooses how many shares they want to sell
def click_to_sell(x, y):

  global shares_owned, current_cash, new_price

  shares_to_sell = input("How many shares would you like to sell? ")
  
  while shares_to_sell.isdigit() == False:
    shares_to_sell = input("Please enter a valid amount of shares: ")

  while int(shares_to_sell) > shares_owned:
    shares_to_sell = input("You do not have that many shares. Please enter a valid amount of shares: ")
 
  while int(shares_to_sell) > 5:
    shares_to_sell = input("You can only sell up to 5 shares at a time. Please enter a valid amount of shares: ")
  
  shares_to_sell = int(shares_to_sell)

  shares_owned -= shares_to_sell
 
  current_cash += shares_to_sell * new_price

  #updates shares and cash on screen
  update_shares_owned()
  update_current_cash()
  update_account_value()
  update_profit_loss()

  print()
  print("Click on the results!")
  
#handles the nothing option
def click_to_nothing(x, y):
  print("Click on the results button to see what would have happened if you bought or sold!") 

#allows users to click on the option they want
def click_user_options():
  buy.onclick(click_to_buy)
  sell.onclick(click_to_sell)
  nothing.onclick(click_to_nothing)
 
#account value turtle to update on screen
def initial_account_value():
  account_value_text.penup()
  account_value_text.pencolor(random_color)
  account_value_text.goto(-280, -180)
  account_value_text.clear()
  account_value_text.write("Account Value: ${:.2f}".format(real_starting_account_value), align = "center", font = ("Arial", 14, "bold"))

#shows the current account value on screen
def update_account_value():
  global current_account_value
  
  account_value_text.penup()
  account_value_text.pencolor(random_color)
  account_value_text.goto(-280, -180)
  account_value_text.clear()
  account_value_text.write("Account Value: ${:.2f}".format(current_account_value), align = "center", font = ("Arial", 14, "bold"))

# sets up game
def play_game():
  
  clear_screen()
  stock_chosen_text()
  turtle_on_screen_during_game()
  name_in_cat()
  update_shares_owned()
  update_current_cash()
  initial_account_value()
  initial_profit_loss()
  event_on_screen()
  click_user_options()
  results_btn()
  print()
  print("Click on the image of the action you want to do.")
  print()
  sel = False

#function to update the profit or loss on screen
def update_profit_loss():
  global current_account_value, real_starting_account_value

  #calculates profit or loss
  current_profit_loss = current_account_value - real_starting_account_value

  profit_loss.penup()
  profit_loss.pencolor(random_color)
  profit_loss.goto(-280, -220)
  profit_loss.clear()
  profit_loss.write("Profit / Loss: ${:.2f}".format(current_profit_loss), align = "center", font = ("Arial", 14, "bold"))
  
  return current_profit_loss

#draws fireworks in celebration screen
def draw_fireworks(x, y, size, color):
  fireworks.speed(0)
  fireworks.penup()
  fireworks.goto(x, y)
  fireworks.pencolor(color)
  fireworks.pendown()

  for i in range(8):
    fireworks.forward(size)
    fireworks.backward(size)
    fireworks.left(45)


#displays celebration on screen
def celebration_screen(x, y):

  clear_screen()
  s.bgcolor("yellow")
  
  s.addshape("catfront.gif")
  celebrate_front.shape("catfront.gif")
  celebrate_front.penup()
  celebrate_front.goto(-165, 0)

  s.addshape("catback.gif")
  celebrate_back.shape("catback.gif")
  celebrate_back.penup()
  celebrate_back.goto(165, 0)

  s.tracer(20)
  for i in range(50):
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    size = random.randint(20, 30)
    color = random.choice(["blue", "red", "orange", "purple", "green"])
    draw_fireworks(x, y, size, color)

  celebration_text.penup()
  celebration_text.goto(0, 0)
  celebration_text.pencolor("green")
  celebration_text.write("YOU GAINED ${:.2f}".format(profit_or_loss) + "!!!", align="center", font = ("Arial", 32, "bold"))

  print("Thank you for playing! You are a natural!")

#when user loses money, this screen shows up 
def losing_screen(x, y):
  clear_screen()

  s.bgcolor("gray")

  s.addshape("sad.gif")
  sad.shape("sad.gif")
  sad.penup()
  sad.goto(0, 0)

  tears_falling()

  sad_screen_text.penup()
  sad_screen_text.goto(0, 0)
  sad_screen_text.pencolor("red")
  sad_screen_text.write("YOU LOST ${:.2f}".format(profit_or_loss * -1) + "!!!", align = "center", font = ("Arial", 32, "bold"))

  print("Thank you for playing! You'll get it next time!")


#shows results button on screen
def results_btn():
  s.addshape("results.gif")
  results.shape("results.gif")
  results.penup()
  results.goto(0, -200)

#animation for tears
def tears_falling():
  
  for i in range(10):

    x_offset = random.randint(-10, 10)
    y_offset = random.randint(-10, 10)

    #tears on left eye
    x1 = sad.xcor() - 35 + x_offset
    y1 = sad.ycor() + 50 - i * 20
    tears.speed(0)
    tears.penup()
    tears.goto(x1, y1)
    tears.dot(10, "lightblue")
    
    #tears on right eye
    x2 = sad.xcor() + 35 - x_offset
    y2 = sad.ycor() + 50 - i * 20
    tears.speed(0)
    tears.penup()
    tears.goto(x2, y2)
    tears.dot(10, "lightblue")
  
#variable to access all events and price changes
all_events = load_events()

#access to a single random event
event_at_random = random_event()

#intial start screen
start_screen()
#opens rules screen in terminal
rules_screen()

#asks user for a name and gets ready to place it inside cat
name = input("Please enter a username: ")

#username must be less than 9 characters
if len(name) > 8:
  name = name[:8]
elif len(name) < 1:
  name = "User1"  

#asks user for which stock they want buy/sell or do neither with
exit_input = ""
while exit_input != "x":
  print()
  #prints out all options for user to enter
  print("1. Apple          2. Amazon")
  print("3. Meta           4. Google")
  print("5. Microsoft      6. Netflix")
  print("7. Walmart        8. Disney")
  print("9. Starbucks      10. Tesla")
  print()
  #asks user for which stock they want buy/sell or do neither with
  stock_input = input("\nPlease enter the name of a company from the list above: ")
  #makes sure the input only capitalizes the first letter
  stock_input = stock_input.capitalize()

  #user must enter a valid stock option
  while stock_input not in stock_price_dict:
    stock_input = input("That is not a valid company. Please choose one from the list above: ")
    stock_input = stock_input.capitalize()

 
  #how much money the stock changes based off the event
  impacted_price = stock_price_dict[stock_input] * all_events[event_at_random]
  new_price = stock_price_dict[stock_input] + impacted_price

  real_starting_account_value = current_cash + (shares_owned * stock_price_dict[stock_input])
  current_account_value = current_cash + (shares_owned * new_price)

  play_game()  

  profit_or_loss = current_account_value - real_starting_account_value

  #puts up correct screen based off profit / loss
  if profit_or_loss > 0:
    results.onclick(celebration_screen)
  else:
    results.onclick(losing_screen)
  
  #ends loop
  exit_input = "x"


turtle.done()


s.mainloop() # this is needed to run turtle graphics
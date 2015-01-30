# encoding=utf-8
'''
设计自动售货机
'''


#另外涉及一些dp的东西。 可以preprocess。   需要找的钱 。  以及多少个硬币。

'''
class drinks :  id, price, name

class VendingMachine
	- boolean takeMoney(Money money);
	//Here item will contain type & quantity, no smart search required
	//say user need half litere Coke.
	- Item pickItem(Item item);
	- boolean isAvailable(Item item)
	- Double askForAmount(Input input);
	- Double valiDateAndReturnBalance(Money money);
class Money
	-CurrencyType type;
	-Double amount
class MoneyValidator
    - boolean validate(Money amount);
class Item
	-ItemType type;
	-Double quantity
	-String barcode; // May be anything else to identify it
class Input
    - CommandType type;
    - Double quantity
	- ItemType type;
class display
    - void updateDisplay(String instructions)
class KeyPad
    - Input readUserInput(Key key);
class Key
    -KeyType type
    -Double value

enum CurrencyType
enum ItemType
enum KeyType
enum CommandType
'''


'''
 UserInterface
Class MoneyValidator can be merged with Class Money itself (this class will have enough info regarding the value of currency and cost should be passed as parameter to validate function)
'''




'''
Interface Iteam{
	id
	price
	discription
	inventory
	sell(){
	//reduce inventory
	}
}

Class Menu{
	Map<Id,Iteam> iteams;
	display(){
		return iteams.values();
	}

	Iteam select(int id){
		return items.get(id);
	}
}

class vandingMachine{
	Menu menu;
	start(){
		menu.display();
	}

	getUserInput(id){
		Iteam selection = menu.select(id);
		Order order = new Order(selection);
		order.process();
		(order.status==sucess){
			dispatch(selectio);
		}
	}

	dispatch(){

	}
}

class Order{
	Iteam iteam;
	PaymentManager payment;
	Status
	acceptPayment(){

	}
	process(){
		if(payment.isSucess()){
			iteam.sell();
		}
	}

}

PaymentManager{
	PaymentStatus {SUCESS,PENDING,FAILED};
	charge(double Price){

	}
}
'''

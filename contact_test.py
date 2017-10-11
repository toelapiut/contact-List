import unittest #Import the unitted module
from contact import Contact #importing contact class
import pyperclip

class Test(unittest.TestCase):


	def setUp(self):
		self.new_contact=Contact('apiut','Toel','071235698','toelapiut7@gmail.com')
			
	def test_init(self):
		self.assertEqual(self.new_contact.first_name,'apiut')
		self.assertEqual(self.new_contact.last_name,'Toel')
		self.assertEqual(self.new_contact.phone_number,'071235698')
		self.assertEqual(self.new_contact.email,'toelapiut7@gmail.com')


	def test_save_contact(self):


		self.new_contact.save_contact()
		self.assertEqual(len(Contact.contact_list),1)

    
	def tearDown(self) :

		Contact.contact_list=[]

	def test_save_multiple_contact(self):

		self.new_contact.save_contact()
		self.test_concat=Contact("Test","user","01235464","test@user.com")

		self.test_concat.save_contact()
		self.assertEqual(len(Contact.contact_list),2)

	def test_delete_contact(self):
		
		self.new_contact.save_contact()
		self.test_concat=Contact("Test","user","01235464","test@user.com")

		self.test_concat.save_contact()
		self.new_contact.delete_contact()
		self.assertEqual(len(Contact.contact_list),1)


	def test_find_contact_by_number(self):

		self.new_contact.save_contact()
		self.test_concat = Contact("Test","user","0711223344","test@user.com")
		self.test_concat.save_contact()


		found_contact=Contact.find_by_number("0711223344")

		self.assertEqual(found_contact.phone_number,self.test_concat.phone_number)


	def test_contact_exists(self):
		self.new_contact.save_contact()
		test_concat=Contact("Test","user","0711223344","test@user.com")
		test_concat.save_contact()

		contact_exist=Contact.contact_exist("0711223344")

		self.assertTrue(contact_exist)

	def test_display_all_contact(self):
		self.assertEqual(Contact.display_contact(),Contact.contact_list)

	def test_copy_email(self):
		self.new_contact.save_contact()
		Contact.copy_email("071235698")

		self.assertEqual(self.new_contact.email,pyperclip.paste())
    

if __name__=='__main__':
	unittest.main(verbosity=2)


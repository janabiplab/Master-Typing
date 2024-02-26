from time import *
import random as r

# this function  find the error
def find_error(para_input,user_input):
    error=0
    for i in range(len(para_input)):
        if i<=len(user_input)-1:
            if para_input[i]==user_input[i]:
                continue
            else:
                error+=1
        else:
            error+=1               
    return error    

# this function find the accuracy
def find_accuracy(error,para_input):
    n=len(para_input)
    new_error=n-error
    accuracy=int((new_error*100)/n)
    return accuracy
# this function find the time in second
def time_taken(time_start,time_end,user_input):
    time_delay=time_end-time_start
    length=len(user_input)
    time_delay=(round(time_delay,2))
    speed=(time_delay/length)
    speed=int(speed)
    return speed



            



# # all type of english test
# # chose raandom  text from your test
if __name__=="__main__":
    for i in range(100):
        check=input("Ready to start(yes/no):"  )
        if check=="yes":
            your_test=["DSA is defined as a combination of two separate yet interrelated topics – Data Structure and Algorithms. DSA is one of the most important skills that every computer science student must have. It is often seen that people with good knowledge of these technologies are better programmers than others and thus, crack the interviews of almost every tech giant.",
           "Applied mathematics is the application of mathematical methods by different fields such as physics, engineering, medicine, biology, finance, business, computer science, and industry. Thus, applied mathematics is a combination of mathematical science and specialized knowledge.",
           "With more than 8,000,000,000 people on the planet today, our population has become so large that the Earth cannot cope. It took until the early 1800s for the world population to reach one billion. Now we add a billion every 12-15 years.",
           "Physics is the natural science of matter, involving the study of matter, its fundamental constituents, its motion and behavior through space and time, and the related entities of energy and force.",
           "Bharatanatyam is based on performance and aesthetic ideas outlined in classics such as Bharata’s Natyashastra. It offers a large collection of songs in Telugu, Tamil, and Sanskrit. The topics include a wide variety of human and heavenly love, and are commonly classified as shringara (romantic love) and Bhakti (devotion). Bharatanatyam music is part of the Carnatic system of music from southern India.",
           "Srinivasa Ramanujan FRS was an Indian mathematician. Though he had almost no formal training in pure mathematics, he made substantial contributions to mathematical analysis, number theory, infinite series, and continued fractions, including solutions to mathematical problems then considered unsolvable.",
           "Kathak is the main dance of northern India, and it is still extensively practised in Uttar Pradesh, Rajasthan, Delhi, Madhya Pradesh, and even regions of western and eastern India. It is said to be related to the storytelling art of Kathakaras, or storytellers, who have for centuries taught the scriptures, the epics Ramayana and Mahabharata, and puranic literature to the general people.",
           "The Andaman Islands are an Indian archipelago in the Bay of Bengal. These roughly 300 islands are known for their palm-lined, white-sand beaches, mangroves and tropical rainforests. Coral reefs supporting marine life such as sharks and rays make for popular diving and snorkeling sites. Indigenous Andaman Islanders inhabit the more remote islands, many of which are off limits to visitors. ",
           "The Pacific Ocean is the largest and deepest of Earth's five oceanic divisions. It extends from the Arctic Ocean in the north to the Southern Ocean in the south, and is bounded by the continents of Asia and Oceania in the west and the Americas in the east.",
           "In 1967, he was honored with the Padma Shri award by the Government of India. In 2001, Rafi was honoured with the Best Singer of the Millennium title by Hero Honda and Stardust magazine. In 2013, Rafi was voted for the Greatest Voice in Hindi Cinema in the CNN-IBN's poll.",
           "Arjuna, also known as Partha and Dhananjaya, a protagonist of the Hindu epic Mahabharata. In the epic he is the third of five Pandava brothers, from the lineage of the Kuru. In the Mahabharata War, Arjuna was a key warrior from the Pandava side and killed many warriors",
           "India is a land of various cultures and a rich heritage. It is the seventh-largest country by area and the second-most populous country globally. The peacock is India's national bird, and the Bengal tiger is the country's national animal. The national song is named Vande Matram."]
            print()
            print("_____________________________________Master Typing_________________________________")
            # for sapce 
            print()
            print()
            # typing for user input
            text=r.choice(your_test)
            print(text)
            # Again space
            print()
            print()

            # time : before typing start yhe user
            time1=time()

            # taking the user input
            user_input=input("Type Here:  ")

            # after the typing end of the time in typing
            time2=time()

            # convert the test in list and remove the space 
            x=list(text.split())

            # convert the user_input  in list and remove the space 
            y=list(user_input.split())

            # calling the function for  finding the error
            error=find_error(x,y)

            # calling ther function for finding accuracy
            accuracy=find_accuracy(error,x)

            # calling the function for t_taken 
            t_taken=time_taken(time1,time2,y)
           
            print("Errors :" ,error)
            print("Accuracy :",accuracy,"%")
            print("WPS :",t_taken)
        elif check=="no":
            print("Thank You")   
            break
        else:
            print("wrong input")
            




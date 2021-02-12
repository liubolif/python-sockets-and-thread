import socket
from datetime import datetime

address = ('localhost', 44444)
max_size = 1024

print('Starting the CLIENT at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)
# якщо ставити блокування тут - то воно ні на що не впливало
client.setblocking(False)

#message = "The Indian government is considering finalising the rules for a new set of labour codes that could provide companies with the flexibility of reducing the total number of working days in a week to four. However, it would mean that employees will have to work 12 hours in a shift, instead of the standard nine.Apurva Chandra, India's Labour and Employment Secretary, told news outlets that many organisations were interested in providing a four-day work week for employees....It is possible that an employer may provide for a five-day working week and I have come across employers who say that we want even a 4-day working week. We have tried to bring in some flexibility into the workdays, he was quoted as saying during a press conference.The 48 hours-per-week limit, however, shall remain. It is sacrosanct, maintained Mr Chandra. The government clarified that companies may have the option to choose a four-day week but employees will have to adjust to 12-hour-long shifts. Mr Chandra added that an organisation opting for a four-day work week will have to provide employees with three days of consecutive holidays.Under the new rules, the government has also proposed free medical check-ups for workers through the Employees State Insurance Corporation, a social security and health insurance scheme for workers.Rule-making process is already underway and likely to complete in the coming week, said the ministry in its official press release.The ministry also announced that it would launch a portal for unorganised labour sector which would collect relevant information on building and construction workers and help to formulate health, housing, skill, insurance, credit and food schemes for migrant workers. The website is expected to be launched by May or June this year.Of course, Labour has to oppose attempts to water down our workers' rights, but if the past decade has taught us anything, it's that a defensive campaign is a losing one. Ed Miliband, the current shadow business secretary, learned that the hard way in 2015, as did Jeremy Corbyn over Brexit.Therefore, the best way to fight the government's proposed dismantling of workers’ rights is to set out a positive vision detailing a better future of work in which workers rights are extended.By this logic, if the government threatens to remove existing working time regulations, then Labour should seek to expand them. When they challenge the 48 hour working week, Labour should be demanding a four-day (32 hour) working week with no loss of pay to give people something worth fighting for.The case for a four-day week should be obvious by now. Under the existing working time regulations, more than two-thirds report being stressed or overworked in their job and research by the Health and Safety Executive showed a shocking 18 million working days were lost in 2019/20 as a result of work-related stress, depression or anxiety......"*10000+"THE END"
message = "Loooooong massage "*100000 + "THE END"

n = client.send(message.encode('utf-8'))
print(n)
client.close()


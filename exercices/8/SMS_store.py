class SMS_Store:
    def __init__(self) -> None:
        self.sms = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        sms = (False, from_number, time_arrived, text_of_SMS)
        self.sms.append(sms)
    
    def message_count(self):
        return len(self.sms)
    
    def get_unread_indexes(self):
        lst = []
        for i in range(self.message_count()):
            if self.sms[i][0] == False:
                lst.append(i)
        return lst

    def get_message(self, i):
        try:
            sms = self.sms[i]
            self.delete(i)
            sms_read = (True, sms[1], sms[2], sms[3])
            self.sms.append(sms_read)
            return (sms[1], sms[2], sms[3])
        except Exception:
            return None

    def delete(self, i):
        del(self.sms[i])

    def clear(self):
        self.sms = []

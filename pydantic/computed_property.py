from pydantic import BaseModel, computed_field, Field

class Booking(BaseModel):
    user_id : int
    room_no : int
    rate_per_night : float
    no_of_nights : int = Field(..., ge = 1)

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.rate_per_night*self.no_of_nights
    
book = Booking(user_id=123, room_no=789, rate_per_night=100.0, no_of_nights=2)
print(book.total_amount)
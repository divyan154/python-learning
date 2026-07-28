# To Visualize This think of comments on any post --- comments are list of comment 

from pydantic import BaseModel
from typing import Optional

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[list['Comment']] = None

Comment.model_rebuild()     #have to run for performance optimizations

comments = Comment(id=1, content="efweefwfew",replies=[Comment(id=2,content="Second comment"), Comment(id=3,content="Third COmment")])
print(comments)
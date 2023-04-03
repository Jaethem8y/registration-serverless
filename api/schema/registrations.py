from pydantic import BaseModel
import typing as typ

class RegistrationNew(BaseModel):
    term: typ.Optional[typ.List[str]] = None   
    subject:typ.Optional[typ.List[str]] = None
    section:typ.Optional[typ.List[str]] = None
    campus:typ.Optional[typ.List[str]] = None
    credit:typ.Optional[typ.List[int]] = None
    title:typ.Optional[typ.List[str]] = None
    days:typ.Optional[typ.List[str]] = None
    start_time:typ.Optional[str] = None
    end_time:typ.Optional[str] = None
    instructor:typ.Optional[typ.List[str]] = None
    attribute:typ.Optional[typ.List[str]] = None 
    

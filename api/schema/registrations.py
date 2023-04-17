from pydantic import BaseModel
import typing as typ

class RegistrationNew(BaseModel):
    term: typ.Optional[typ.List[str]] = []  
    subject:typ.Optional[typ.List[str]] = []
    section:typ.Optional[typ.List[str]] = []
    campus:typ.Optional[typ.List[str]] = []
    credit:typ.Optional[typ.List[int]] = []
    title:typ.Optional[typ.List[str]] = []
    days:typ.Optional[typ.List[str]] = []
    start_time:typ.Optional[str] = None
    end_time:typ.Optional[str] = None
    instructor:typ.Optional[typ.List[str]] = []
    attribute:typ.Optional[typ.List[str]] = [] 
    

class RegistrationLegacy(BaseModel):
    term: typ.Optional[typ.List[str]] = None   
    subject: typ.Optional[typ.List[str]] = None
    title: typ.Optional[typ.List[str]] = None
    campus: typ.Optional[typ.List[str]] = None
    type: typ.Optional[typ.List[str]] = None
    last_name: typ.Optional[typ.List[str]] = None
    first_name: typ.Optional[typ.List[str]] = None

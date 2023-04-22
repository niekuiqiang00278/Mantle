from root.base.wrapper.EvsWrapper import EvsWrapper
from root.utils.StateUtils import StateUtils
from root.plux.XState import XSkin
from pydantic import BaseModel
from pydantic import BaseModel, create_model

class JesHit:
    def __init__(self):
        pass

    @XSkin()
    def km0(self, state: StateUtils):
        print('km0')
        state.errn('fff')

    @XSkin()
    def km1(self, state: StateUtils):
        print('km1')


class JesBis(JesHit):
    def __init__(self):
        JesHit.__init__(self)

    @EvsWrapper()
    def k0(self, state: StateUtils):
        self.km0(state=state)
        self.km1(state=state)


if __name__ == '__main__':
    from pydantic import BaseModel, create_model

    user_dict = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "ww":{
            'wwc':'wf'
        }
    }

    User = type("User", (BaseModel,), user_dict)
    print(User.schema())
    class Ww:
        wwc:str
    class User:
        id:int
        name:str
        email:str
        ww:Ww
    #
    # User = create_model(
    #     "User",
    #     **user_dict
    # )
    #
    # class_definition = User.__fields__
    # class_name = User.__name__
    #
    # field_definitions = "\n".join([f"    {key}: {value.type_.__name__}" for key, value in class_definition.items()])
    #
    # model_definition = f"class {class_name}(BaseModel):\n{field_definitions}\n\n    class Config:\n        title = '{class_name}'"
    #
    # print(model_definition)
class Q_PERSONA:
    def __init__(V_PERSONA, name, age, alive, occupation):
        V_PERSONA.name = name
        V_PERSONA.age = age
        V_PERSONA.alive = alive
        V_PERSONA.occupation = occupation

    def F_GET_NAME(V_PERSONA):
        return V_PERSONA.name

    def F_GET_AGE(V_PERSONA):
        return V_PERSONA.age

    def F_IS_ALIVE(V_PERSONA):
        return V_PERSONA.alive

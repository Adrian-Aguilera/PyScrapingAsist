from Class.ControllerApp import EngineApp
import os

if __name__ == "__main__":
    Engine = EngineApp(EngineDef=True, EngineIA=False)
    Engine.main_engine() # Llamamos a la clase
    
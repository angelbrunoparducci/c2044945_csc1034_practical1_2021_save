#!/usr/bin/env python

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


def else__():
    pass


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False,  scale=1, remove_panda=False, stop_walk=False):


        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if no_rotate == False:
            print("spin")
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        print("load_panda")

        if remove_panda:
            ""
        else:
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            size = 0.005*scale
            self.pandaActor.setScale(size, size, size)
            self.pandaActor.reparentTo(self.render)
            # Loop its animations
        if stop_walk:
            ""
        else:
            self.pandaActor.loop("walk")

        mySound = self.loader.loadSfx("Sounds/cats.mp3")
        mySound.play()


    # Define a procedure to move the camera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

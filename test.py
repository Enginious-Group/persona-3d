import os
import maya.standalone
maya.standalone.initialize("Python")
import logging
logging.basicConfig(level=logging.DEBUG)
# TODO: logi
import maya.cmds as cmds
import maya.mel as mel


scene_path = "Karen_M_M_full_rig.mb"
path_to_asset = "Input/baked_new_topology.obj"

def open_scene():
    cmds.file(new=True, force=True)
    cmds.file(scene_path, open=True)

def load_plugins():

    # cmds.loadPlugin("fbxmaya")
    # cmds.loadPlugin("gameFbxExporter")
    # #its needed to manually place those in MAYA_PLUG_IN_PATH
    # cmds.loadPlugin("embeddedRL4")
    # cmds.loadPlugin("MayaUE4RBFPlugin2022")
    # cmds.loadPlugin("MayaUERBFPlugin")
    cmds.loadPlugin(allPlugins = True)

def import_persona_mesh():
    cmds.file(path_to_asset, i=True, ignoreVersion=True, type="OBJ", namespace="baked_new_topology", pr=True, importFrameRate=True,importTimeRange="override")

def init_movement():
    cmds.select('baked_new_topology:Mesh', r=True)
    cmds.move(0, 0, 161.35, r = True)
    cmds.rotate( 90, 0, 0, r = True, os = True, fo = True)
    cmds.move(0, -6, 0, r = True)
    cmds.rotate( 3.6, 0, 0, r = True, os = True, fo = True)

def export_result():
    cmds.select('baked_new_topology:Mesh')
    cmds.select('eyeshell_lod0_mesh', d=True)
    cmds.select('eyeEdge_lod0_mesh', d=True)
    cmds.select('cartilage_lod0_mesh', d=True)

load_plugins()
open_scene()
mel.eval('batch-mel.mel')

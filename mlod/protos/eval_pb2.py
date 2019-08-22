# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlod/protos/eval.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlod/protos/eval.proto',
  package='mlod.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x16mlod/protos/eval.proto\x12\x0bmlod.protos\"\xe2\x01\n\nEvalConfig\x12\x1a\n\reval_interval\x18\x01 \x01(\r:\x03\x35\x30\x30\x12\x16\n\teval_mode\x18\x02 \x01(\t:\x03val\x12\x14\n\x0c\x63kpt_indices\x18\x03 \x03(\x05\x12!\n\x13\x65valuate_repeatedly\x18\x04 \x01(\x08:\x04true\x12#\n\x14\x61llow_gpu_mem_growth\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\"\n\x15kitti_score_threshold\x18\x06 \x01(\x02:\x03\x30.1\x12\x1e\n\x13\x65valuation_fraction\x18\x07 \x01(\x02:\x01\x31')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EVALCONFIG = _descriptor.Descriptor(
  name='EvalConfig',
  full_name='mlod.protos.EvalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eval_interval', full_name='mlod.protos.EvalConfig.eval_interval', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=500,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_mode', full_name='mlod.protos.EvalConfig.eval_mode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("val").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ckpt_indices', full_name='mlod.protos.EvalConfig.ckpt_indices', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluate_repeatedly', full_name='mlod.protos.EvalConfig.evaluate_repeatedly', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_gpu_mem_growth', full_name='mlod.protos.EvalConfig.allow_gpu_mem_growth', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kitti_score_threshold', full_name='mlod.protos.EvalConfig.kitti_score_threshold', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluation_fraction', full_name='mlod.protos.EvalConfig.evaluation_fraction', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=266,
)

DESCRIPTOR.message_types_by_name['EvalConfig'] = _EVALCONFIG

EvalConfig = _reflection.GeneratedProtocolMessageType('EvalConfig', (_message.Message,), dict(
  DESCRIPTOR = _EVALCONFIG,
  __module__ = 'mlod.protos.eval_pb2'
  # @@protoc_insertion_point(class_scope:mlod.protos.EvalConfig)
  ))
_sym_db.RegisterMessage(EvalConfig)


# @@protoc_insertion_point(module_scope)

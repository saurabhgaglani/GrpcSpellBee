# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spellbee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spellbee.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0espellbee.proto\"%\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"\x1e\n\rletterRequest\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"!\n\x0eletterResponse\x12\x0f\n\x07numbers\x18\x01 \x03(\t\"\x1d\n\x0cscoreRequest\x12\r\n\x05input\x18\x01 \x01(\t\"\x1e\n\rscoreResponse\x12\r\n\x05score\x18\x01 \x01(\r\")\n\x0bwordRequest\x12\x0b\n\x03num\x18\x01 \x03(\t\x12\r\n\x05input\x18\x02 \x01(\t\"\x1b\n\x0cwordResponse\x12\x0b\n\x03res\x18\x01 \x01(\t\"\x1c\n\x0b\x64ictRequest\x12\r\n\x05input\x18\x01 \x01(\t\"\x1b\n\x0c\x64ictResponse\x12\x0b\n\x03res\x18\x01 \x01(\t\"\'\n\x0e\x63onnectRequest\x12\x15\n\x04play\x18\x01 \x01(\x0b\x32\x07.Player\" \n\x0f\x63onnectResponse\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\" \n\rstateResponse\x12\x0f\n\x07players\x18\x01 \x03(\t\"\x1f\n\x0bgameRequest\x12\x10\n\x08gameOver\x18\x01 \x01(\x08\"\x1d\n\x0cgameResponse\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"\x1d\n\x0cstateRequest\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"\x1b\n\nendRequest\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"!\n\x0b\x65ndResponse\x12\x12\n\ngameIsOver\x18\x01 \x01(\x08\"\x1f\n\rwinnerRequest\x12\x0e\n\x06winner\x18\x01 \x01(\t\"\x1f\n\x0ewinnerResponse\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"!\n\x10getWinnerRequest\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\"#\n\x11getWinnerResponse\x12\x0e\n\x06winner\x18\x01 \x01(\t\"\x1f\n\x0egetGameRequest\x12\r\n\x05\x65mpty\x18\x01 \x01(\t\" \n\x0fgetGameresponse\x12\r\n\x05games\x18\x01 \x01(\x05\x32\x94\x04\n\x06Server\x12/\n\ngetLetters\x12\x0e.letterRequest\x1a\x0f.letterResponse\"\x00\x12+\n\x08getScore\x12\r.scoreRequest\x1a\x0e.scoreResponse\"\x00\x12*\n\tcheckWord\x12\x0c.wordRequest\x1a\r.wordResponse\"\x00\x12*\n\tcheckDict\x12\x0c.dictRequest\x1a\r.dictResponse\"\x00\x12\x32\n\x0fgetCurrentState\x12\r.stateRequest\x1a\x0e.stateResponse\"\x00\x12-\n\x0cgameHasEnded\x12\x0c.gameRequest\x1a\r.gameResponse\"\x00\x12+\n\x0chasGameEnded\x12\x0b.endRequest\x1a\x0c.endResponse\"\x00\x12\x32\n\rdeclareWinner\x12\x0e.winnerRequest\x1a\x0f.winnerResponse\"\x00\x12\x34\n\tgetWinner\x12\x11.getWinnerRequest\x1a\x12.getWinnerResponse\"\x00\x12\x32\n\x0bgetNumGames\x12\x0f.getGameRequest\x1a\x10.getGameresponse\"\x00\x12&\n\x07\x63onnect\x12\x07.Player\x1a\x10.connectResponse\"\x00\x62\x06proto3'
)




_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='Player.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=55,
)


_LETTERREQUEST = _descriptor.Descriptor(
  name='letterRequest',
  full_name='letterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='letterRequest.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=87,
)


_LETTERRESPONSE = _descriptor.Descriptor(
  name='letterResponse',
  full_name='letterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='letterResponse.numbers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=122,
)


_SCOREREQUEST = _descriptor.Descriptor(
  name='scoreRequest',
  full_name='scoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='scoreRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=153,
)


_SCORERESPONSE = _descriptor.Descriptor(
  name='scoreResponse',
  full_name='scoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='scoreResponse.score', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=185,
)


_WORDREQUEST = _descriptor.Descriptor(
  name='wordRequest',
  full_name='wordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='wordRequest.num', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input', full_name='wordRequest.input', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=228,
)


_WORDRESPONSE = _descriptor.Descriptor(
  name='wordResponse',
  full_name='wordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='wordResponse.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=257,
)


_DICTREQUEST = _descriptor.Descriptor(
  name='dictRequest',
  full_name='dictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='dictRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=287,
)


_DICTRESPONSE = _descriptor.Descriptor(
  name='dictResponse',
  full_name='dictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='dictResponse.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=316,
)


_CONNECTREQUEST = _descriptor.Descriptor(
  name='connectRequest',
  full_name='connectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='connectRequest.play', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=357,
)


_CONNECTRESPONSE = _descriptor.Descriptor(
  name='connectResponse',
  full_name='connectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='connectResponse.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=391,
)


_STATERESPONSE = _descriptor.Descriptor(
  name='stateResponse',
  full_name='stateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='players', full_name='stateResponse.players', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=425,
)


_GAMEREQUEST = _descriptor.Descriptor(
  name='gameRequest',
  full_name='gameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameOver', full_name='gameRequest.gameOver', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=458,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='gameResponse',
  full_name='gameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='gameResponse.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=489,
)


_STATEREQUEST = _descriptor.Descriptor(
  name='stateRequest',
  full_name='stateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='stateRequest.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=520,
)


_ENDREQUEST = _descriptor.Descriptor(
  name='endRequest',
  full_name='endRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='endRequest.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=522,
  serialized_end=549,
)


_ENDRESPONSE = _descriptor.Descriptor(
  name='endResponse',
  full_name='endResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameIsOver', full_name='endResponse.gameIsOver', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=584,
)


_WINNERREQUEST = _descriptor.Descriptor(
  name='winnerRequest',
  full_name='winnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='winner', full_name='winnerRequest.winner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=617,
)


_WINNERRESPONSE = _descriptor.Descriptor(
  name='winnerResponse',
  full_name='winnerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='winnerResponse.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=650,
)


_GETWINNERREQUEST = _descriptor.Descriptor(
  name='getWinnerRequest',
  full_name='getWinnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='getWinnerRequest.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=652,
  serialized_end=685,
)


_GETWINNERRESPONSE = _descriptor.Descriptor(
  name='getWinnerResponse',
  full_name='getWinnerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='winner', full_name='getWinnerResponse.winner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=722,
)


_GETGAMEREQUEST = _descriptor.Descriptor(
  name='getGameRequest',
  full_name='getGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='getGameRequest.empty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=755,
)


_GETGAMERESPONSE = _descriptor.Descriptor(
  name='getGameresponse',
  full_name='getGameresponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='games', full_name='getGameresponse.games', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=789,
)

_CONNECTREQUEST.fields_by_name['play'].message_type = _PLAYER
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['letterRequest'] = _LETTERREQUEST
DESCRIPTOR.message_types_by_name['letterResponse'] = _LETTERRESPONSE
DESCRIPTOR.message_types_by_name['scoreRequest'] = _SCOREREQUEST
DESCRIPTOR.message_types_by_name['scoreResponse'] = _SCORERESPONSE
DESCRIPTOR.message_types_by_name['wordRequest'] = _WORDREQUEST
DESCRIPTOR.message_types_by_name['wordResponse'] = _WORDRESPONSE
DESCRIPTOR.message_types_by_name['dictRequest'] = _DICTREQUEST
DESCRIPTOR.message_types_by_name['dictResponse'] = _DICTRESPONSE
DESCRIPTOR.message_types_by_name['connectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['connectResponse'] = _CONNECTRESPONSE
DESCRIPTOR.message_types_by_name['stateResponse'] = _STATERESPONSE
DESCRIPTOR.message_types_by_name['gameRequest'] = _GAMEREQUEST
DESCRIPTOR.message_types_by_name['gameResponse'] = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['stateRequest'] = _STATEREQUEST
DESCRIPTOR.message_types_by_name['endRequest'] = _ENDREQUEST
DESCRIPTOR.message_types_by_name['endResponse'] = _ENDRESPONSE
DESCRIPTOR.message_types_by_name['winnerRequest'] = _WINNERREQUEST
DESCRIPTOR.message_types_by_name['winnerResponse'] = _WINNERRESPONSE
DESCRIPTOR.message_types_by_name['getWinnerRequest'] = _GETWINNERREQUEST
DESCRIPTOR.message_types_by_name['getWinnerResponse'] = _GETWINNERRESPONSE
DESCRIPTOR.message_types_by_name['getGameRequest'] = _GETGAMEREQUEST
DESCRIPTOR.message_types_by_name['getGameresponse'] = _GETGAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:Player)
  })
_sym_db.RegisterMessage(Player)

letterRequest = _reflection.GeneratedProtocolMessageType('letterRequest', (_message.Message,), {
  'DESCRIPTOR' : _LETTERREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:letterRequest)
  })
_sym_db.RegisterMessage(letterRequest)

letterResponse = _reflection.GeneratedProtocolMessageType('letterResponse', (_message.Message,), {
  'DESCRIPTOR' : _LETTERRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:letterResponse)
  })
_sym_db.RegisterMessage(letterResponse)

scoreRequest = _reflection.GeneratedProtocolMessageType('scoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCOREREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:scoreRequest)
  })
_sym_db.RegisterMessage(scoreRequest)

scoreResponse = _reflection.GeneratedProtocolMessageType('scoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCORERESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:scoreResponse)
  })
_sym_db.RegisterMessage(scoreResponse)

wordRequest = _reflection.GeneratedProtocolMessageType('wordRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORDREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:wordRequest)
  })
_sym_db.RegisterMessage(wordRequest)

wordResponse = _reflection.GeneratedProtocolMessageType('wordResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORDRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:wordResponse)
  })
_sym_db.RegisterMessage(wordResponse)

dictRequest = _reflection.GeneratedProtocolMessageType('dictRequest', (_message.Message,), {
  'DESCRIPTOR' : _DICTREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:dictRequest)
  })
_sym_db.RegisterMessage(dictRequest)

dictResponse = _reflection.GeneratedProtocolMessageType('dictResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICTRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:dictResponse)
  })
_sym_db.RegisterMessage(dictResponse)

connectRequest = _reflection.GeneratedProtocolMessageType('connectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:connectRequest)
  })
_sym_db.RegisterMessage(connectRequest)

connectResponse = _reflection.GeneratedProtocolMessageType('connectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:connectResponse)
  })
_sym_db.RegisterMessage(connectResponse)

stateResponse = _reflection.GeneratedProtocolMessageType('stateResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATERESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:stateResponse)
  })
_sym_db.RegisterMessage(stateResponse)

gameRequest = _reflection.GeneratedProtocolMessageType('gameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:gameRequest)
  })
_sym_db.RegisterMessage(gameRequest)

gameResponse = _reflection.GeneratedProtocolMessageType('gameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:gameResponse)
  })
_sym_db.RegisterMessage(gameResponse)

stateRequest = _reflection.GeneratedProtocolMessageType('stateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATEREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:stateRequest)
  })
_sym_db.RegisterMessage(stateRequest)

endRequest = _reflection.GeneratedProtocolMessageType('endRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:endRequest)
  })
_sym_db.RegisterMessage(endRequest)

endResponse = _reflection.GeneratedProtocolMessageType('endResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENDRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:endResponse)
  })
_sym_db.RegisterMessage(endResponse)

winnerRequest = _reflection.GeneratedProtocolMessageType('winnerRequest', (_message.Message,), {
  'DESCRIPTOR' : _WINNERREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:winnerRequest)
  })
_sym_db.RegisterMessage(winnerRequest)

winnerResponse = _reflection.GeneratedProtocolMessageType('winnerResponse', (_message.Message,), {
  'DESCRIPTOR' : _WINNERRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:winnerResponse)
  })
_sym_db.RegisterMessage(winnerResponse)

getWinnerRequest = _reflection.GeneratedProtocolMessageType('getWinnerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWINNERREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:getWinnerRequest)
  })
_sym_db.RegisterMessage(getWinnerRequest)

getWinnerResponse = _reflection.GeneratedProtocolMessageType('getWinnerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETWINNERRESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:getWinnerResponse)
  })
_sym_db.RegisterMessage(getWinnerResponse)

getGameRequest = _reflection.GeneratedProtocolMessageType('getGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGAMEREQUEST,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:getGameRequest)
  })
_sym_db.RegisterMessage(getGameRequest)

getGameresponse = _reflection.GeneratedProtocolMessageType('getGameresponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGAMERESPONSE,
  '__module__' : 'spellbee_pb2'
  # @@protoc_insertion_point(class_scope:getGameresponse)
  })
_sym_db.RegisterMessage(getGameresponse)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=792,
  serialized_end=1324,
  methods=[
  _descriptor.MethodDescriptor(
    name='getLetters',
    full_name='Server.getLetters',
    index=0,
    containing_service=None,
    input_type=_LETTERREQUEST,
    output_type=_LETTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getScore',
    full_name='Server.getScore',
    index=1,
    containing_service=None,
    input_type=_SCOREREQUEST,
    output_type=_SCORERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='checkWord',
    full_name='Server.checkWord',
    index=2,
    containing_service=None,
    input_type=_WORDREQUEST,
    output_type=_WORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='checkDict',
    full_name='Server.checkDict',
    index=3,
    containing_service=None,
    input_type=_DICTREQUEST,
    output_type=_DICTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getCurrentState',
    full_name='Server.getCurrentState',
    index=4,
    containing_service=None,
    input_type=_STATEREQUEST,
    output_type=_STATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='gameHasEnded',
    full_name='Server.gameHasEnded',
    index=5,
    containing_service=None,
    input_type=_GAMEREQUEST,
    output_type=_GAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hasGameEnded',
    full_name='Server.hasGameEnded',
    index=6,
    containing_service=None,
    input_type=_ENDREQUEST,
    output_type=_ENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='declareWinner',
    full_name='Server.declareWinner',
    index=7,
    containing_service=None,
    input_type=_WINNERREQUEST,
    output_type=_WINNERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getWinner',
    full_name='Server.getWinner',
    index=8,
    containing_service=None,
    input_type=_GETWINNERREQUEST,
    output_type=_GETWINNERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getNumGames',
    full_name='Server.getNumGames',
    index=9,
    containing_service=None,
    input_type=_GETGAMEREQUEST,
    output_type=_GETGAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='connect',
    full_name='Server.connect',
    index=10,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_CONNECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)

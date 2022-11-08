# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: substreams.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import modules_pb2 as modules__pb2
import clock_pb2 as clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10substreams.proto\x12\x10sf.substreams.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\rmodules.proto\x1a\x0b\x63lock.proto\"\x93\x02\n\x07Request\x12\x17\n\x0fstart_block_num\x18\x01 \x01(\x03\x12\x14\n\x0cstart_cursor\x18\x02 \x01(\t\x12\x16\n\x0estop_block_num\x18\x03 \x01(\x04\x12.\n\nfork_steps\x18\x04 \x03(\x0e\x32\x1a.sf.substreams.v1.ForkStep\x12!\n\x19irreversibility_condition\x18\x05 \x01(\t\x12*\n\x07modules\x18\x06 \x01(\x0b\x32\x19.sf.substreams.v1.Modules\x12\x16\n\x0eoutput_modules\x18\x07 \x03(\t\x12*\n\"initial_store_snapshot_for_modules\x18\x08 \x03(\t\"\xb9\x02\n\x08Response\x12\x30\n\x07session\x18\x05 \x01(\x0b\x32\x1d.sf.substreams.v1.SessionInitH\x00\x12\x35\n\x08progress\x18\x01 \x01(\x0b\x32!.sf.substreams.v1.ModulesProgressH\x00\x12>\n\rsnapshot_data\x18\x02 \x01(\x0b\x32%.sf.substreams.v1.InitialSnapshotDataH\x00\x12\x46\n\x11snapshot_complete\x18\x03 \x01(\x0b\x32).sf.substreams.v1.InitialSnapshotCompleteH\x00\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.sf.substreams.v1.BlockScopedDataH\x00\x42\t\n\x07message\"\x1f\n\x0bSessionInit\x12\x10\n\x08trace_id\x18\x01 \x01(\t\")\n\x17InitialSnapshotComplete\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\"\x80\x01\n\x13InitialSnapshotData\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12-\n\x06\x64\x65ltas\x18\x02 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltas\x12\x11\n\tsent_keys\x18\x04 \x01(\x04\x12\x12\n\ntotal_keys\x18\x03 \x01(\x04\"\xa4\x01\n\x0f\x42lockScopedData\x12/\n\x07outputs\x18\x01 \x03(\x0b\x32\x1e.sf.substreams.v1.ModuleOutput\x12&\n\x05\x63lock\x18\x03 \x01(\x0b\x32\x17.sf.substreams.v1.Clock\x12(\n\x04step\x18\x06 \x01(\x0e\x32\x1a.sf.substreams.v1.ForkStep\x12\x0e\n\x06\x63ursor\x18\n \x01(\t\"\xad\x01\n\x0cModuleOutput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\nmap_output\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x35\n\x0cstore_deltas\x18\x03 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasH\x00\x12\x0c\n\x04logs\x18\x04 \x03(\t\x12\x16\n\x0elogs_truncated\x18\x05 \x01(\x08\x42\x06\n\x04\x64\x61ta\"D\n\x0fModulesProgress\x12\x31\n\x07modules\x18\x01 \x03(\x0b\x32 .sf.substreams.v1.ModuleProgress\"\xc4\x04\n\x0eModuleProgress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x10processed_ranges\x18\x02 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedRangeH\x00\x12\x46\n\rinitial_state\x18\x03 \x01(\x0b\x32-.sf.substreams.v1.ModuleProgress.InitialStateH\x00\x12J\n\x0fprocessed_bytes\x18\x04 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedBytesH\x00\x12\x39\n\x06\x66\x61iled\x18\x05 \x01(\x0b\x32\'.sf.substreams.v1.ModuleProgress.FailedH\x00\x1aH\n\x0eProcessedRange\x12\x36\n\x10processed_ranges\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.BlockRange\x1a-\n\x0cInitialState\x12\x1d\n\x15\x61vailable_up_to_block\x18\x02 \x01(\x04\x1aG\n\x0eProcessedBytes\x12\x18\n\x10total_bytes_read\x18\x01 \x01(\x04\x12\x1b\n\x13total_bytes_written\x18\x02 \x01(\x04\x1a>\n\x06\x46\x61iled\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0c\n\x04logs\x18\x02 \x03(\t\x12\x16\n\x0elogs_truncated\x18\x03 \x01(\x08\x42\x06\n\x04type\"4\n\nBlockRange\x12\x13\n\x0bstart_block\x18\x02 \x01(\x04\x12\x11\n\tend_block\x18\x03 \x01(\x04\";\n\x0bStoreDeltas\x12,\n\x06\x64\x65ltas\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.StoreDelta\"\xc7\x01\n\nStoreDelta\x12\x39\n\toperation\x18\x01 \x01(\x0e\x32&.sf.substreams.v1.StoreDelta.Operation\x12\x0f\n\x07ordinal\x18\x02 \x01(\x04\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x11\n\told_value\x18\x04 \x01(\x0c\x12\x11\n\tnew_value\x18\x05 \x01(\x0c\":\n\tOperation\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\x81\x01\n\x06Output\x12\x11\n\tblock_num\x18\x01 \x01(\x04\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x05value\x18\n \x01(\x0b\x32\x14.google.protobuf.Any*\\\n\x08\x46orkStep\x12\x10\n\x0cSTEP_UNKNOWN\x10\x00\x12\x0c\n\x08STEP_NEW\x10\x01\x12\r\n\tSTEP_UNDO\x10\x02\x12\x15\n\x11STEP_IRREVERSIBLE\x10\x04\"\x04\x08\x03\x10\x03\"\x04\x08\x05\x10\x05\x32K\n\x06Stream\x12\x41\n\x06\x42locks\x12\x19.sf.substreams.v1.Request\x1a\x1a.sf.substreams.v1.Response0\x01\x42\x46ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreamsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'substreams_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreams'
  _FORKSTEP._serialized_start=2372
  _FORKSTEP._serialized_end=2464
  _REQUEST._serialized_start=127
  _REQUEST._serialized_end=402
  _RESPONSE._serialized_start=405
  _RESPONSE._serialized_end=718
  _SESSIONINIT._serialized_start=720
  _SESSIONINIT._serialized_end=751
  _INITIALSNAPSHOTCOMPLETE._serialized_start=753
  _INITIALSNAPSHOTCOMPLETE._serialized_end=794
  _INITIALSNAPSHOTDATA._serialized_start=797
  _INITIALSNAPSHOTDATA._serialized_end=925
  _BLOCKSCOPEDDATA._serialized_start=928
  _BLOCKSCOPEDDATA._serialized_end=1092
  _MODULEOUTPUT._serialized_start=1095
  _MODULEOUTPUT._serialized_end=1268
  _MODULESPROGRESS._serialized_start=1270
  _MODULESPROGRESS._serialized_end=1338
  _MODULEPROGRESS._serialized_start=1341
  _MODULEPROGRESS._serialized_end=1921
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_start=1657
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_end=1729
  _MODULEPROGRESS_INITIALSTATE._serialized_start=1731
  _MODULEPROGRESS_INITIALSTATE._serialized_end=1776
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_start=1778
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_end=1849
  _MODULEPROGRESS_FAILED._serialized_start=1851
  _MODULEPROGRESS_FAILED._serialized_end=1913
  _BLOCKRANGE._serialized_start=1923
  _BLOCKRANGE._serialized_end=1975
  _STOREDELTAS._serialized_start=1977
  _STOREDELTAS._serialized_end=2036
  _STOREDELTA._serialized_start=2039
  _STOREDELTA._serialized_end=2238
  _STOREDELTA_OPERATION._serialized_start=2180
  _STOREDELTA_OPERATION._serialized_end=2238
  _OUTPUT._serialized_start=2241
  _OUTPUT._serialized_end=2370
  _STREAM._serialized_start=2466
  _STREAM._serialized_end=2541
# @@protoc_insertion_point(module_scope)

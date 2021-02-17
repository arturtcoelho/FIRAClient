// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: command.proto

#ifndef PROTOBUF_INCLUDED_command_2eproto
#define PROTOBUF_INCLUDED_command_2eproto

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3006001
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_command_2eproto 

namespace protobuf_command_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[2];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
}  // namespace protobuf_command_2eproto
namespace fira_message {
namespace sim_to_ref {
class Command;
class CommandDefaultTypeInternal;
extern CommandDefaultTypeInternal _Command_default_instance_;
class Commands;
class CommandsDefaultTypeInternal;
extern CommandsDefaultTypeInternal _Commands_default_instance_;
}  // namespace sim_to_ref
}  // namespace fira_message
namespace google {
namespace protobuf {
template<> ::fira_message::sim_to_ref::Command* Arena::CreateMaybeMessage<::fira_message::sim_to_ref::Command>(Arena*);
template<> ::fira_message::sim_to_ref::Commands* Arena::CreateMaybeMessage<::fira_message::sim_to_ref::Commands>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace fira_message {
namespace sim_to_ref {

// ===================================================================

class Command : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:fira_message.sim_to_ref.Command) */ {
 public:
  Command();
  virtual ~Command();

  Command(const Command& from);

  inline Command& operator=(const Command& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  Command(Command&& from) noexcept
    : Command() {
    *this = ::std::move(from);
  }

  inline Command& operator=(Command&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const Command& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Command* internal_default_instance() {
    return reinterpret_cast<const Command*>(
               &_Command_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(Command* other);
  friend void swap(Command& a, Command& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline Command* New() const final {
    return CreateMaybeMessage<Command>(NULL);
  }

  Command* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<Command>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const Command& from);
  void MergeFrom(const Command& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Command* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // uint32 id = 1;
  void clear_id();
  static const int kIdFieldNumber = 1;
  ::google::protobuf::uint32 id() const;
  void set_id(::google::protobuf::uint32 value);

  // bool yellowteam = 2;
  void clear_yellowteam();
  static const int kYellowteamFieldNumber = 2;
  bool yellowteam() const;
  void set_yellowteam(bool value);

  // double wheel_left = 6;
  void clear_wheel_left();
  static const int kWheelLeftFieldNumber = 6;
  double wheel_left() const;
  void set_wheel_left(double value);

  // double wheel_right = 7;
  void clear_wheel_right();
  static const int kWheelRightFieldNumber = 7;
  double wheel_right() const;
  void set_wheel_right(double value);

  // @@protoc_insertion_point(class_scope:fira_message.sim_to_ref.Command)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 id_;
  bool yellowteam_;
  double wheel_left_;
  double wheel_right_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_command_2eproto::TableStruct;
};
// -------------------------------------------------------------------

class Commands : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:fira_message.sim_to_ref.Commands) */ {
 public:
  Commands();
  virtual ~Commands();

  Commands(const Commands& from);

  inline Commands& operator=(const Commands& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  Commands(Commands&& from) noexcept
    : Commands() {
    *this = ::std::move(from);
  }

  inline Commands& operator=(Commands&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const Commands& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Commands* internal_default_instance() {
    return reinterpret_cast<const Commands*>(
               &_Commands_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(Commands* other);
  friend void swap(Commands& a, Commands& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline Commands* New() const final {
    return CreateMaybeMessage<Commands>(NULL);
  }

  Commands* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<Commands>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const Commands& from);
  void MergeFrom(const Commands& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Commands* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // repeated .fira_message.sim_to_ref.Command robot_commands = 1;
  int robot_commands_size() const;
  void clear_robot_commands();
  static const int kRobotCommandsFieldNumber = 1;
  ::fira_message::sim_to_ref::Command* mutable_robot_commands(int index);
  ::google::protobuf::RepeatedPtrField< ::fira_message::sim_to_ref::Command >*
      mutable_robot_commands();
  const ::fira_message::sim_to_ref::Command& robot_commands(int index) const;
  ::fira_message::sim_to_ref::Command* add_robot_commands();
  const ::google::protobuf::RepeatedPtrField< ::fira_message::sim_to_ref::Command >&
      robot_commands() const;

  // @@protoc_insertion_point(class_scope:fira_message.sim_to_ref.Commands)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::RepeatedPtrField< ::fira_message::sim_to_ref::Command > robot_commands_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_command_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// Command

// uint32 id = 1;
inline void Command::clear_id() {
  id_ = 0u;
}
inline ::google::protobuf::uint32 Command::id() const {
  // @@protoc_insertion_point(field_get:fira_message.sim_to_ref.Command.id)
  return id_;
}
inline void Command::set_id(::google::protobuf::uint32 value) {
  
  id_ = value;
  // @@protoc_insertion_point(field_set:fira_message.sim_to_ref.Command.id)
}

// bool yellowteam = 2;
inline void Command::clear_yellowteam() {
  yellowteam_ = false;
}
inline bool Command::yellowteam() const {
  // @@protoc_insertion_point(field_get:fira_message.sim_to_ref.Command.yellowteam)
  return yellowteam_;
}
inline void Command::set_yellowteam(bool value) {
  
  yellowteam_ = value;
  // @@protoc_insertion_point(field_set:fira_message.sim_to_ref.Command.yellowteam)
}

// double wheel_left = 6;
inline void Command::clear_wheel_left() {
  wheel_left_ = 0;
}
inline double Command::wheel_left() const {
  // @@protoc_insertion_point(field_get:fira_message.sim_to_ref.Command.wheel_left)
  return wheel_left_;
}
inline void Command::set_wheel_left(double value) {
  
  wheel_left_ = value;
  // @@protoc_insertion_point(field_set:fira_message.sim_to_ref.Command.wheel_left)
}

// double wheel_right = 7;
inline void Command::clear_wheel_right() {
  wheel_right_ = 0;
}
inline double Command::wheel_right() const {
  // @@protoc_insertion_point(field_get:fira_message.sim_to_ref.Command.wheel_right)
  return wheel_right_;
}
inline void Command::set_wheel_right(double value) {
  
  wheel_right_ = value;
  // @@protoc_insertion_point(field_set:fira_message.sim_to_ref.Command.wheel_right)
}

// -------------------------------------------------------------------

// Commands

// repeated .fira_message.sim_to_ref.Command robot_commands = 1;
inline int Commands::robot_commands_size() const {
  return robot_commands_.size();
}
inline void Commands::clear_robot_commands() {
  robot_commands_.Clear();
}
inline ::fira_message::sim_to_ref::Command* Commands::mutable_robot_commands(int index) {
  // @@protoc_insertion_point(field_mutable:fira_message.sim_to_ref.Commands.robot_commands)
  return robot_commands_.Mutable(index);
}
inline ::google::protobuf::RepeatedPtrField< ::fira_message::sim_to_ref::Command >*
Commands::mutable_robot_commands() {
  // @@protoc_insertion_point(field_mutable_list:fira_message.sim_to_ref.Commands.robot_commands)
  return &robot_commands_;
}
inline const ::fira_message::sim_to_ref::Command& Commands::robot_commands(int index) const {
  // @@protoc_insertion_point(field_get:fira_message.sim_to_ref.Commands.robot_commands)
  return robot_commands_.Get(index);
}
inline ::fira_message::sim_to_ref::Command* Commands::add_robot_commands() {
  // @@protoc_insertion_point(field_add:fira_message.sim_to_ref.Commands.robot_commands)
  return robot_commands_.Add();
}
inline const ::google::protobuf::RepeatedPtrField< ::fira_message::sim_to_ref::Command >&
Commands::robot_commands() const {
  // @@protoc_insertion_point(field_list:fira_message.sim_to_ref.Commands.robot_commands)
  return robot_commands_;
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace sim_to_ref
}  // namespace fira_message

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_command_2eproto

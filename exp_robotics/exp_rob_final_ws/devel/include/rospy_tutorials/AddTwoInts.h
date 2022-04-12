// Generated by gencpp from file rospy_tutorials/AddTwoInts.msg
// DO NOT EDIT!


#ifndef ROSPY_TUTORIALS_MESSAGE_ADDTWOINTS_H
#define ROSPY_TUTORIALS_MESSAGE_ADDTWOINTS_H

#include <ros/service_traits.h>


#include <rospy_tutorials/AddTwoIntsRequest.h>
#include <rospy_tutorials/AddTwoIntsResponse.h>


namespace rospy_tutorials
{

struct AddTwoInts
{

typedef AddTwoIntsRequest Request;
typedef AddTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTwoInts
} // namespace rospy_tutorials


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rospy_tutorials::AddTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::rospy_tutorials::AddTwoInts&) { return value(); }
};

template<>
struct DataType< ::rospy_tutorials::AddTwoInts > {
  static const char* value()
  {
    return "rospy_tutorials/AddTwoInts";
  }

  static const char* value(const ::rospy_tutorials::AddTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::rospy_tutorials::AddTwoIntsRequest> should match
// service_traits::MD5Sum< ::rospy_tutorials::AddTwoInts >
template<>
struct MD5Sum< ::rospy_tutorials::AddTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rospy_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::rospy_tutorials::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rospy_tutorials::AddTwoIntsRequest> should match
// service_traits::DataType< ::rospy_tutorials::AddTwoInts >
template<>
struct DataType< ::rospy_tutorials::AddTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::rospy_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::rospy_tutorials::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rospy_tutorials::AddTwoIntsResponse> should match
// service_traits::MD5Sum< ::rospy_tutorials::AddTwoInts >
template<>
struct MD5Sum< ::rospy_tutorials::AddTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rospy_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::rospy_tutorials::AddTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rospy_tutorials::AddTwoIntsResponse> should match
// service_traits::DataType< ::rospy_tutorials::AddTwoInts >
template<>
struct DataType< ::rospy_tutorials::AddTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::rospy_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::rospy_tutorials::AddTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROSPY_TUTORIALS_MESSAGE_ADDTWOINTS_H
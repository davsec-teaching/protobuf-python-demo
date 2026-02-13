# Generated using cursor. 

import person_pb2

def test_person_serialization():
    # Create a Person message
    person = person_pb2.Person()
    person.user_name = "Alice"
    person.favourite_number = 42
    person.interests.extend(["reading", "hiking", "coding"])

    # Serialize the message to bytes
    serialized_data = person.SerializeToString()

    # Deserialize the bytes back to a Person message
    deserialized_person = person_pb2.Person()
    deserialized_person.ParseFromString(serialized_data)

    # Assert that the original and deserialized messages are the same
    assert person == deserialized_person, "Deserialized message does not match the original"
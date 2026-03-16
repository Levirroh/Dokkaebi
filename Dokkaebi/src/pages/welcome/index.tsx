import Message from '@/src/components/message';
import { HeaderTitle } from '@react-navigation/elements';
import { useState } from 'react';
import { Button, StyleSheet, Text, TextInput, View } from 'react-native';

export type Props = {
  name: string;
};

function Welcome({ name }: Props) {
  const [isOpen, setIsOpen] = useState(false);

  function changeModal() {
    setIsOpen(!isOpen)
  }

  return (
    <View style={styles.container}>
      <View style={styles.greeting}>
        <HeaderTitle>Dokkaebi</HeaderTitle>
        <TextInput placeholder='Login' style={styles.input} />
        <TextInput placeholder='Password' secureTextEntry={true} style={styles.input} />
        <Button
          title="Entrar"
          color="orange"
          onPress={changeModal}
        />
        <Message isShown={isOpen} onClose={changeModal} duration={3} message={"Usuário ou senha inválidos"}></Message>
      </View>
    </View> 
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  greeting: {
    fontSize: 20,
    fontWeight: 'bold',
    margin: 16,
  },
  overlay: {
    flex: 1, 
    backgroundColor: 'rgba(0, 0, 0, 0.5)', 
    justifyContent: 'center', 
    alignItems: 'center', 
  },
  title: {
    textAlign: 'center',
  },
  buttonContainer: {
    alignContent: 'center',
  },
  input: {
    backgroundColor: 'gray',
    color: 'black',
  },
  modalCard: {
    width: '30%', 
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 20,
    elevation: 5,
  },
});

export default Welcome;
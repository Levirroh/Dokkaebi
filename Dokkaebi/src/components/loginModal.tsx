import { HeaderTitle } from '@react-navigation/elements';
import { Button, Modal, StyleSheet, Text, TextInput, View } from 'react-native';

export type Props = {
  isOpen: boolean;
  onClose: () => void;
};


function LoginModal({ isOpen }: Props) {
  function onClose(){
    isOpen = false;
  }

  function Login(){
    isOpen = false;
  }

  return (
    <Modal visible={isOpen} transparent={true} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modalCard}>
          <Text style={styles.title}>Acesso Dokkaebi</Text>

          <TextInput placeholder='Login' style={styles.input} />
          <TextInput placeholder='Password' secureTextEntry={true} style={styles.input} />

          <View style={styles.buttonContainer}>
            <Button title="Cancelar" color="red" onPress={onClose} />
            <Button title="Entrar" onPress={() => { Login }} />
          </View>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
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

export default LoginModal;
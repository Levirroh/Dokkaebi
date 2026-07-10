import { HeaderTitle } from '@react-navigation/elements';
import { Button, Modal, StyleSheet, Text, TextInput, View } from 'react-native';

export type Props = {
  isShown: boolean;
  duration: number;
  message: string;
  options?: MessageOption[] | null;
  onClose: () => void;
};

export type MessageOption = {
  onClick: () => void;
};

function Message({ isShown, duration, message, options, onClose }: Props) {

  function Login(){
    onClose();
  }

  return (
    <Modal visible={isShown} style={styles.modalCard} transparent={true} animationType="fade">
    </Modal>
  );
}

const styles = StyleSheet.create({
  modalCard: {
    width: '30%', 
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 20,
    elevation: 5,
  },
});

export default Message;
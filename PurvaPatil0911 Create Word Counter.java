import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class WordCharacterParagraphCounter extends JFrame {
    private JTextArea textArea;
    private JLabel wordCountLabel;
    private JLabel characterCountLabel;
    private JLabel paragraphCountLabel;

    public WordCharacterParagraphCounter() {
        setTitle("Word, Character, and Paragraph Counter");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane, BorderLayout.CENTER);

        JPanel countPanel = new JPanel(new GridLayout(3, 2));

        JLabel wordLabel = new JLabel("Word Count:");
        wordCountLabel = new JLabel("0");
        JLabel characterLabel = new JLabel("Character Count:");
        characterCountLabel = new JLabel("0");
        JLabel paragraphLabel = new JLabel("Paragraph Count:");
        paragraphCountLabel = new JLabel("0");

        countPanel.add(wordLabel);
        countPanel.add(wordCountLabel);
        countPanel.add(characterLabel);
        countPanel.add(characterCountLabel);
        countPanel.add(paragraphLabel);
        countPanel.add(paragraphCountLabel);

        add(countPanel, BorderLayout.SOUTH);

        textArea.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = textArea.getText();
                int wordCount = countWords(text);
                int characterCount = countCharacters(text);
                int paragraphCount = countParagraphs(text);

                wordCountLabel.setText(String.valueOf(wordCount));
                characterCountLabel.setText(String.valueOf(characterCount));
                paragraphCountLabel.setText(String.valueOf(paragraphCount));
            }
        });

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private int countWords(String text) {
        String[] words = text.split("\\s+");
        return words.length;
    }

    private int countCharacters(String text) {
        return text.length();
    }

    private int countParagraphs(String text) {
        String[] paragraphs = text.split("\\n\\s*\\n");
        return paragraphs.length;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new WordCharacterParagraphCounter();
            }
        });
    }
}
 

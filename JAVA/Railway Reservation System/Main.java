package railway;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main extends javax.swing.JFrame {

    public Main() {
        initComponents();
    }

    private void initComponents() {
        
        JButton addTrainButton = new JButton("Add Train");
        JButton reservationButton = new JButton("Reservation");
        JButton bookingsButton = new JButton("Bookings");

       
        JLabel servicesLabel = new JLabel("Services");
        servicesLabel.setFont(new Font("Arial", Font.BOLD, 20));  
        servicesLabel.setForeground(new Color(0, 123, 255));  
        servicesLabel.setHorizontalAlignment(SwingConstants.CENTER);

        
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Welcome to Railway System");
        setSize(500, 450);  
        setLocationRelativeTo(null);  

        
        getContentPane().setBackground(new Color(245, 245, 245));  
        setLayout(new GridBagLayout());  

        
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;  
        gbc.gridy = 0;  
        gbc.insets = new Insets(10, 10, 10, 10);  

        
        add(servicesLabel, gbc);
        
        
        customizeButton(addTrainButton);
        customizeButton(reservationButton);
        customizeButton(bookingsButton);

        
        gbc.gridy = 1;  
        gbc.gridwidth = 1;  
        add(addTrainButton, gbc);
        
        gbc.gridy = 2;  
        add(reservationButton, gbc);
        
        gbc.gridy = 3;  
        add(bookingsButton, gbc);

        
        addTrainButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                addtrain addTrainPage = new addtrain();  
                addTrainPage.setVisible(true);
                dispose();  
            }
        });

        
        reservationButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                Reservation reservationPage = new Reservation();  
                reservationPage.setVisible(true);
                dispose();  
            }
        });

        
        bookingsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                Bookings bookingsPage = new Bookings();  
                bookingsPage.setVisible(true);
                dispose();  
            }
        });
    }

    
    private void customizeButton(JButton button) {
        
        button.setFont(new Font("Arial", Font.BOLD, 16));  

        
        button.setBackground(new Color(0, 123, 255));  
        button.setForeground(Color.WHITE);  
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createLineBorder(new Color(0, 123, 255), 2, true));
        button.setOpaque(true);
        button.setPreferredSize(new Dimension(200, 50));  

        
        button.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                button.setBackground(new Color(0, 150, 255));  
            }

            public void mouseExited(java.awt.event.MouseEvent evt) {
                button.setBackground(new Color(0, 123, 255));  
            }
        });
    }

    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
}

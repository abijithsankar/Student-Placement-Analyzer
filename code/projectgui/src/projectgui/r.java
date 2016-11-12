/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package projectgui;
import java.awt.Component;
import java.io.*;
import javax.swing.JOptionPane;
/**
 *
 * @author Mithus
 */
public class r extends javax.swing.JFrame{
private static Component frame;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        
        // TODO code application logic here
        String call="python C:\\Users\\Mithus\\Documents\\NetBeansProjects\\projectgui\\code.py";
        Runtime.getRuntime().exec(call);
        BufferedReader in = new BufferedReader(new FileReader("C:/Users/Mithus/Documents/NetBeansProjects/projectgui/result.txt"));
        String line;
        while((line = in.readLine()) != null)
            {
                JOptionPane.showMessageDialog(frame, line);

        in.close();
            
    }
    }

    
}

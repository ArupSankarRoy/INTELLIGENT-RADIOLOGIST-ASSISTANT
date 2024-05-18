import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import shutil

def plot_multiple_plots():
    try:
        # Setup paths
        root = os.getcwd()
        pred_folder = os.path.join(root, 'Pred')
        path = os.path.join(pred_folder, 'predictions.csv')
        
        # Read the CSV file
        df = pd.read_csv(path)

        # Round the values to three decimal places and multiply by 100
        rounded_df = df.iloc[0, :].apply(lambda x: round(x, 3) * 100).reset_index()
        rounded_df.columns = ['index', 'value']
        rounded_df['index'] = ["Abnormalities", "ACL_Tear", "Meniscal_Tear"]

        # Setting up the plot style
        sns.set_style("whitegrid")
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

        # Bar plot
        ax1 = sns.barplot(x='index', y='value', hue='index', data=rounded_df, palette="viridis", ax=axes[0, 0], legend=False)
        ax1.set_title('MRI Predictions - Bar Plot')
        ax1.set_ylabel('Percentage')
        for p in ax1.patches:
            ax1.annotate(f"{p.get_height():.1f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', fontsize=12, color='gray', xytext=(0, 5),
                         textcoords='offset points')

        # Pie plot
        ax2 = axes[0, 1]
        ax2.pie(rounded_df['value'], labels=rounded_df['index'], autopct='%1.1f%%', startangle=90, 
                colors=sns.color_palette('viridis', len(rounded_df['index'])))
        ax2.axis('equal')
        ax2.set_title('MRI Predictions - Pie Plot')

        # Line plot
        ax3 = axes[1, 0]
        ax3.plot(rounded_df['index'], rounded_df['value'], marker='o', color='skyblue', linestyle='-')
        ax3.set_title('MRI Predictions - Line Plot')
        ax3.set_ylabel('Percentage')

        # Stacked bar plot
        ax4 = axes[1, 1]
        stacked_df = pd.DataFrame({
            'index': rounded_df['index'],
            'Positive': rounded_df['value'],
            'Negative': 100 - rounded_df['value']
        })
        stacked_df.plot(x='index', kind='bar', stacked=True, ax=ax4, color=['skyblue', 'salmon'])
        ax4.set_title('MRI Predictions - Stacked Bar Plot')
        ax4.set_ylabel('Percentage')

        # Save the plots as an image
        plot_dir_path = os.path.join(os.getcwd(), 'static')
        if os.path.exists(plot_dir_path):
            shutil.rmtree(plot_dir_path)
        os.makedirs(plot_dir_path, exist_ok=True)
        plt.savefig(os.path.join(plot_dir_path, 'predictions_plot.png'))

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close(fig)  # Close the figure






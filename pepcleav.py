import pandas as pd
import argparse
import os

Level_rank_dict = {
"High_High": 'Level 5',
"High_Medium": 'Level 4',
"Medium_High": 'Level 4',
"Medium_Medium": 'Level 3',
"High_Low": 'Level 3',
"Low_High": 'Level 3',
"Low_Medium": 'Level 2',
"Medium_Low": 'Level 2',
"Low_Low": 'Level 1',
}

Rank_dict = {
"High_High": 5,
"High_Medium": 4,
"Medium_High": 4,
"Medium_Medium": 3,
"High_Low": 3,
"Low_High": 3,
"Low_Medium": 2,
"Medium_Low": 2,
"Low_Low": 1,
}
def main(args):
    C_file = args.C_terminus
    N_file = args.N_terminus
    input_file = args.input_file
    output_file = args.output_file

    C_AA_list = pd.read_table(C_file, header=0)
    #header: C-terminal_P1 Median_Cleavability Cleavability_Level
    N_AA_list = pd.read_table(N_file, header=0)
    #header: N-terminal_P2 Median_Cleavability Cleavability_Level
    peptides = pd.read_table(input_file, header=0)
    #header: Peptides

    peptides["C-terminal_P1"] = peptides["Peptides"].apply(lambda x: x[-1])
    peptides["N-terminal_P2"] = peptides["Peptides"].apply(lambda x: x[1])
    peptides["C_Cleavability_Level"] = peptides["C-terminal_P1"].apply(lambda x: C_AA_list[C_AA_list["C-terminal_P1"]==x]["Cleavability_Level"].values[0])
    peptides["N_Cleavability_Level"] = peptides["N-terminal_P2"].apply(lambda x: N_AA_list[N_AA_list["N-terminal_P2"]==x]["Cleavability_Level"].values[0])
    peptides["Peptide_Cleavability_Level"] = peptides["C_Cleavability_Level"] + "_" + peptides["N_Cleavability_Level"]
    peptides["Level"] = peptides["Peptide_Cleavability_Level"].apply(lambda x: Level_rank_dict[x])
    peptides["Rank"] = peptides["Peptide_Cleavability_Level"].apply(lambda x: Rank_dict[x])
    peptides["Peptide_Cleavability_Level"] = peptides["Peptide_Cleavability_Level"].astype("category")
    
    peptides.to_csv(output_file, index=False, sep=",")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "--input_file",
        type=str,
        help="Input file (*.csv)",
        required=True,
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default=os.getcwd()+"/PepCleav_result.csv",
        help="Output file (default = ./PepCleav_result.csv)",
        required=False,
    )
    parser.add_argument(
        '--C_terminus',
        default=os.path.dirname(os.path.abspath(__file__))+"/C.list",
        help="C-terminal cleavability",
        required=False,
    )
    parser.add_argument(
        '--N_terminus',
        default=os.path.dirname(os.path.abspath(__file__))+"/N.list",
        help="N-terminal cleavability",
        required=False,
    )
    args = parser.parse_args()
    main(args)

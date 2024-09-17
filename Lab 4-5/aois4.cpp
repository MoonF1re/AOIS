#include"..//aois4/FinalFormsBuilder.cpp"
#include"..//aois4/ManualTruthTable.cpp"
#include"..//aois4/NormalFormsBuilder.cpp"
#include <vector>
#include <iostream>

int main() {
    setlocale(LC_ALL, "ru");
    ManualTruthTable tt;
    tt.manualInput({
        "00000",
        "00110",
        "01010",
        "01101",
        "10010",
        "10101",
        "11001",
        "11111"
        }, { "A", "B", "C", "D", "V" });

    auto combinations = tt.getCombinations();
    auto resultsD = tt.getResultsForVariable("D");
    std::vector<std::string> allVariableNames = { "A", "B", "C" };
    NormalFormsBuilder nfb(combinations, resultsD, allVariableNames, "D");
    std::string mdnfD = nfb.buildMDNF();
    std::cout << "СДНФ для D: " << std::endl;
    std::cout << mdnfD;
    FinalFormsBuilder fb;
    fb.TDNFCalcTable(mdnfD);
    std::cout << std::endl;
    auto resultsV = tt.getResultsForVariable("V");
    std::vector<std::string> allVariableNamesV = { "A", "B", "C" };
    NormalFormsBuilder nfbV(combinations, resultsV, allVariableNamesV, "V");
    std::string mdnfV = nfbV.buildMDNF();
    std::cout << "СДНФ для V: " << std::endl;
    std::cout << mdnfV;
    FinalFormsBuilder fbV;
    fbV.TDNFCalcTable(mdnfV);

    std::cout << "_________________________________________________________" << std::endl;

    ManualTruthTable tt2;
    tt2.manualInput({
        "00000110",
        "00010111",
        "00101000",
        "00111001",
        "01001010",
        "01011011",
        "01101100",
        "01111101",
        "10001110",
        "10011111"
        }, { "A", "B", "C", "D", "E", "F", "J", "H" });
    FinalFormsBuilder fb2;
    auto combinations2 = tt2.getCombinations();
    auto resultsE = tt2.getResultsForVariable("E");
    std::vector<std::string> allVariableNamesE = { "A", "B", "C", "D" };
    NormalFormsBuilder nfbE(combinations2, resultsE, allVariableNamesE, "E");
    std::string mdnfE = nfbE.buildMDNF();
    std::cout << "СДНФ для E: " << std::endl;
    std::cout << mdnfE;
    fb2.TDNFCalcTable(mdnfE);
    std::cout << std::endl;
    auto resultsF = tt2.getResultsForVariable("F");
    std::vector<std::string> allVariableNamesF = { "A", "B", "C", "D" };
    NormalFormsBuilder nfbF(combinations2, resultsF, allVariableNamesF, "F");
    std::string mdnfF = nfbF.buildMDNF();
    std::cout << "СДНФ для F: " << std::endl;
    std::cout << mdnfF;
    fb2.TDNFCalcTable(mdnfF);
    std::cout << std::endl;
    auto resultsJ = tt2.getResultsForVariable("J");
    std::vector<std::string> allVariableNamesJ = { "A", "B", "C", "D" };
    NormalFormsBuilder nfbJ(combinations2, resultsJ, allVariableNamesJ, "J");
    std::string mdnfJ = nfbJ.buildMDNF();
    std::cout << "СДНФ для J: " << std::endl;
    std::cout << mdnfJ;
    fb2.TDNFCalcTable(mdnfJ);
    std::cout << std::endl;
    auto resultsH = tt2.getResultsForVariable("H");
    std::vector<std::string> allVariableNamesH = { "A", "B", "C", "D" };
    NormalFormsBuilder nfbH(combinations2, resultsH, allVariableNamesH, "H");
    std::string mdnfH = nfbH.buildMDNF();
    std::cout << "СДНФ для H: " << std::endl;
    std::cout << mdnfH;
    fb2.TDNFCalcTable(mdnfH);
    return 0;
}

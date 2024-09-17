#pragma once
#include <vector>
#include <string>
#include <map>

class ManualTruthTable {
public:
    inline  void manualInput(const std::vector<std::string>& inputData, const std::vector<std::string>& names);
    std::vector<std::map<std::string, bool>> getCombinations() const;
    std::vector<bool> getResultsForVariable(const std::string& variableName) const;

private:
    std::vector<std::string> variableNames;
    std::vector<std::map<std::string, bool>> combinations;
    std::map<std::string, std::vector<bool>> results;

    inline void printHeader() const;
    inline void printRow(size_t index) const;
};



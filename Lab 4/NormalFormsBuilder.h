#pragma once
#include <vector>
#include <map>
#include <string>

class NormalFormsBuilder {
public:
    inline NormalFormsBuilder(const std::vector<std::map<std::string, bool>>& combinations,
        const std::vector<bool>& results,
        const std::vector<std::string>& variables,
        const std::string& resultVariable);
    inline std::string buildMDNF() const;

private:
    std::vector<std::map<std::string, bool>> combinations;
    std::vector<bool> results;
    std::vector<std::string> variables;
    std::string resultVariable;
};

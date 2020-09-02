
#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
int n = 4,m = 6;
int area[1001] = {0};
int area_cnt[1001] = {0};
pair<int,int> arrow[8] = {
    make_pair(1,0),make_pair(-1,0),make_pair(0,1),make_pair(0,-1),
    make_pair(-1,-1),make_pair(1,-1),make_pair(1,1),make_pair(-1,1)
};
bool check(int x, int y){
    return (x>=0 && x < m) && (y>=0 && y<n);
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int main() {
    int x,y,nx,ny;
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<vector<int> > tmp;
    vector<vector<int> > picture({
        vector<int>({1, 1, 1, 0}),
        vector<int>({1, 2, 2, 0}),
        vector<int>({1, 0, 0, 1}),
        vector<int>({0, 0, 0, 1}),
        vector<int>({0, 0, 0, 3}),
        vector<int>({0, 0, 0, 3}),
    });
    tmp.resize(m, vector<int>(n));
    copy(picture.begin(),picture.end(),tmp.begin());
    for(int i = 0; i<m;i++){
        for(int j = 0; j<n;j++){
            cout<<tmp[i][j];
        }
        cout<<endl;
    }
    
    pair<int,int> xy = make_pair(0,0);
    queue<pair<int,int> > q;
    vector<pair<int,int> > visit;
    int index = 0;
    q.push(xy);
    while(!q.empty()){
        xy = q.front();
        x = xy.first;
        y = xy.second;
        tmp[x][y] = -1;
        q.pop();
        for(int i=0;i<8;i++){
            nx = x + arrow[i].first;
            ny = y + arrow[i].second;
            if(check(nx,ny) && tmp[nx][ny] != -1){
                tmp[nx][ny] = -1;
                q.push(make_pair(nx,ny));
                if((picture[nx][ny] == picture[x][y]) && picture[nx][ny] != 0){
                    area[index] +=1;
                }
                if((picture[nx][ny] != picture[x][y])){
                    area_cnt[index] += 1;
                    cout<< nx << " " << ny << endl;
                    cout<<"현재"<< " " <<x <<" "<<y << " "<<nx<<" " <<ny <<endl;
                    area[picture[nx][ny]];
                    index+=1;
                }
            }
        }
    }
    cout<<"index " << index << endl;
    for(auto i:area){
        if(i != 0){
            cout<<"area "<<i<<endl;
        }
    }
    for(auto i:area_cnt){
        if(i != 0){
            cout<<"area_cnt "<<i<<endl;
        }
    }
    for(int i=0;i<tmp.size();i++){
        for(int j=0; j<tmp[i].size();j++){
            cout<<tmp[i][j]<<"  ";
        }
        cout<< " "<<endl;
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return 0;
}
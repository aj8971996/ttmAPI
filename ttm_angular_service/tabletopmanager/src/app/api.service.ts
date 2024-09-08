import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';  // Replace with your FastAPI base URL

  constructor(private http: HttpClient) {}

  // GM Endpoints

  addCharacter(charData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-character/`, charData);
  }

  addAbility(abilityData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-ability/`, abilityData);
  }

  addExpertise(expertiseData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-expertise/`, expertiseData);
  }

  addJobSkill(jobSkillData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-job-skill/`, jobSkillData);
  }

  addSpeciesPassive(speciesPassiveData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-species-passive/`, speciesPassiveData);
  }

  addItem(itemData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-item/`, itemData);
  }

  addWeapon(weaponData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gm/add-weapon/`, weaponData);
  }

  viewCharacters(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gm/view-characters/`);
  }

  viewLibraries(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gm/view-libraries/`);
  }

  viewBackpacks(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gm/view-backpacks/`);
  }

  viewItems(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gm/view-items/`);
  }

  viewAbilities(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gm/view-abilities/`);
  }

  bulkRemoveItems(removeCriteria: any): Observable<any> {
    return this.http.delete(`${this.apiUrl}/gm/remove-items/`, { body: removeCriteria });
  }

  // Player and GM Endpoints

  addPlayerCharacter(charData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/player/add-character/`, charData);
  }

  viewPlayerCharacter(userId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/view-character/?user_id=${userId}`);
  }

  viewPlayerBackpack(charId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/view-backpack/?char_id=${charId}`);
  }

  viewPlayerLibrary(charId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/view-library/?char_id=${charId}`);
  }

  getAbilityDetails(abilityId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-ability/?ability_id=${abilityId}`);
  }

  getJobSkillDetails(jobSkillId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-job-skill/?job_skill_id=${jobSkillId}`);
  }

  getSpeciesPassiveDetails(speciesPassiveId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-species-passive/?species_passive_id=${speciesPassiveId}`);
  }

  getExpertiseDetails(expertiseId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-expertise/?expertise_id=${expertiseId}`);
  }

  getItemDetails(itemId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-item/?item_id=${itemId}`);
  }

  getWeaponDetails(weaponId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/player/get-weapon/?weapon_id=${weaponId}`);
  }

  levelUpCharacter(charId: number, newLevel: number): Observable<any> {
    const body = { char_id: charId, new_level: newLevel };
    return this.http.post(`${this.apiUrl}/player/level-up/`, body);
  }

  adjustCharacterStats(statsData: any, statAllocation: any, rolledValue: number): Observable<any> {
    // Include logic to adjust stats based on statAllocation and rolledValue
    let totalAllocation = 0;
    const maxStatLimit = 50;

    for (const key in statAllocation) {
      totalAllocation += statAllocation[key];
      statsData[key] = Math.min(maxStatLimit, (statsData[key] || 0) + statAllocation[key]);
    }

    if (totalAllocation > rolledValue) {
      throw new Error("Total allocation exceeds rolled value.");
    }

    return this.http.post(`${this.apiUrl}/player/adjust-stats/`, statsData);
  }

  addItemToBackpack(charId: number, itemId: number): Observable<any> {
    const body = { char_id: charId, item_id: itemId };
    return this.http.post(`${this.apiUrl}/player/add-item/`, body);
  }

  removeItemFromBackpack(charId: number, itemId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/player/remove-item/?char_id=${charId}&item_id=${itemId}`);
  }

  addWeaponToBackpack(charId: number, weaponId: number): Observable<any> {
    const body = { char_id: charId, weapon_id: weaponId };
    return this.http.post(`${this.apiUrl}/player/add-weapon/`, body);
  }

  removeWeaponFromBackpack(charId: number, weaponId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/player/remove-weapon/?char_id=${charId}&weapon_id=${weaponId}`);
  }
}

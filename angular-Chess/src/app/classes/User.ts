import { Guid } from "guid-typescript";

export class User {
    private _name: string;
    private _id: Guid;
    
    constructor(name: string) {
        this._name = name;
        this._id = Guid.create();
    }
    
    get id(): Guid {
        return this._id;
    }
    
    get name(): string {
        return this._name;
    }
    
    set name(newName: string) {
        newName = newName.trim();
        if (newName === "")
        {
            throw new Error("User name must have at least 1 Non-whitespace Character.");
        }
        
        this._name = newName;
    }
}